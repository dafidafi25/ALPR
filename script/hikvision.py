from logging import error
import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth
from requests.sessions import TooManyRedirects
import xmltodict
from urllib.parse import urljoin
import json
from datetime import datetime
import cv2
import numpy as np
import time

def response_parser(response, present='dict'):
    if isinstance(response, (list,)):
        result = "".join(response)
    else:
        result = response.text

    if present == 'dict':
        if isinstance(response, (list,)):
            events = []
            for event in response:
                e = json.loads(json.dumps(xmltodict.parse(event)))
                events.append(e)
            return events
        return json.loads(json.dumps(xmltodict.parse(result)))
    else:
        return result

def dateTimeConvert(data):
        try:
            assert data.find("-")>0
        except AssertionError:
            data= data[:4] + '-' + data[4:]
            data= data[:7] + '-' + data[7:]
            data= data[:13] + ':'+ data[13:]
            data= data[:16] + ':'+ data[16:]
        finally:
            date = data.split('T')
            time= date[1].split('+')
            data = date[0] + " " + time[0]
            data = datetime.strptime(data,'%Y-%m-%d %H:%M:%S')
            # print(data)
            return data

def filterListResponse(data,timeFilter = None):
    timeFilter = timeFilter if timeFilter != None else datetime.min
    arrData=[]
    for x in range(len(data)):
        currPLateTime = dateTimeConvert(data[x]['captureTime'])
        if(currPLateTime > timeFilter):
            arrData.append((data[x]['plateNumber'],currPLateTime))
    return arrData
    


class isapiClient:
    def __init__(self, host, login=None, password=None, timeout=3, isapi_prefix='ISAPI'):
        self.host = host
        self.login = login
        self.password = password
        self.timeout = float(timeout)
        self.isapi_prefix = isapi_prefix
        print(self._check_session())
        self.req,self.valid = self._check_session()
        self.count_events = 1

    def _check_session(self):
        full_url = urljoin(self.host, self.isapi_prefix + '/System/status')
        session = requests.session()
        session.auth = HTTPBasicAuth(self.login, self.password)
        try:
            response = session.get(full_url)
            if response.status_code == 401:
                session.auth = HTTPDigestAuth(self.login, self.password)
                response = session.get(full_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(e)
            return False
            
        else:
            return session,True

    def getNumberPlates(self,time = None):
        payload = "<AfterTime ><picTime>%s</picTime></AfterTime>".format("0")
        try:
            response = self.req.request(
            method='get', url= self.host + "/ISAPI/Traffic/channels/1/vehicleDetect/plates", timeout=self.timeout, stream=True, data=payload)
        except requests.exceptions.RequestException as e:
            print(e)
        else:
            response = response_parser(response)
            if len(response['Plates']) == 3:
                return filterListResponse(response['Plates']['Plate'],time)
            return response

    def systemTime(self):
        response = self.req.request(
        method='get', url= self.host + "/ISAPI/System/time", timeout=self.timeout, stream=True)
        response = response_parser(response)
        response = dateTimeConvert(response['Time']['localTime'])

        return response
    
    def pictureRequest(self):
        response = self.req.request( method='get', url= self.host + "/ISAPI/Streaming/channels/1/picture", timeout=self.timeout, stream=True)
        response.raise_for_status()
        # data = response.json()

        # ##with beautiful soup
        response = self.req.request( method='get', url= self.host + "/ISAPI/Streaming/channels/1/picture", timeout=self.timeout, stream=True).content
        image = np.asarray(bytearray(response), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        # for img sdt(img)
        # response.raise_for_status()
        # data = response.json()

        # # response = response_parser(response)
        # # response = dateTimeConvert(response['Time']['localTime'])

        return image
    
    


if __name__ == "__main__":
    ip = "192.168.2.64"
    port = "80"
    host = 'http://'+ip + ':'+ port
    cam = isapiClient(host, 'admin', '-arngnennscfrer2')
    while True:
        time.sleep(100)
    # img = cam.pictureRequest()

   

    # # for testing
    # cv2.imshow('image',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # cv2.imshow("Image",img)    

    # cv2.waitKey()


