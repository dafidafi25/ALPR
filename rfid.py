from time import sleep
from smartcard.System import readers
from smartcard.util import toHexString
import requests
import json




#Starting connection
device = readers()
connection = device[0].createConnection()
connection.connect()
print('device connected')

authA = '00 00 00 00 00 00'
authB = 'FF FF FF FF FF FF'


def init(): #Initiate so device can start read TAG
    start1 = 'ff 71 13 06 00'  # set SAM communication to contactless
    start1 = bytearray.fromhex(start1)
    start2 = 'ff 71 10 00 00'  # reset SAM communication
    start2 = bytearray.fromhex(start2)
    sendCmd(start1)
    sendCmd(start2)

def setTempAuth(storeNumb,keyNumb): # Load & Set Authentication Key to Reader
    authKey = 'FF 82 00'
    authKey = bytes.fromhex(authKey)
    authKey = authKey + bytes([storeNumb])
    authKey = authKey + bytes([6])
    authKey = authKey + bytes.fromhex(keyNumb)
    sendCmd(authKey)

def sendCmd(cmd): #Send Command to Reader
    # cmd = bytearray.fromhex(cmd)
    cmd = list(cmd)
    # print("Data dikirim ==>  " + toHexString(cmd))
    data, sw1, sw2 = connection.transmit(cmd)
    # print ("response : %x %x" % (sw1, sw2))
    # if len(data) > 0:
        # print('response data : ' + toHexString(data))
    return (sw1,data)

#Authentication to TAG keyTypeA = 0 || keyTypeB = 1
def mifareAuth(blockNumber,keyType):
    auth = 'ff 86 00 00 05 01 00'
    auth = bytearray.fromhex(auth)
    auth = auth + bytes([blockNumber])
    if keyType == 0 :
        auth = auth + bytes([0x60])
        auth = auth + bytes([0])
    elif keyType == 1:
        auth = auth + bytes([0x61])
        auth = auth + bytes([1])
    else:
        return 'Auth Not Valid'
    # print(auth)
    sw1,data = sendCmd(auth)
    return sw1

def readBlock(blockNumber,length,keyType):
    validity = mifareAuth(blockNumber,keyType)

    if  validity == 144:
        readCmd = 'ff b0 00'
        readCmd = bytearray.fromhex(readCmd)
        readCmd += bytes([blockNumber])
        readCmd += bytes([length])
        sw1,data = sendCmd(readCmd)
        return data

def isNewCard(): #Initiate so device can start read TAG
    # start1 = [0xff, 0x71, 0x13, 0x06, 0x00]  # set SAM communication to contactless
    start2 = [0xff, 0x71, 0x10, 0x00, 0x00]  # reset SAM communication
    sw1 ,data = sendCmd(start2)
    if sw1 == 0x90:
        return True
    else:
        return False


if __name__=="__main__":
    init()
    setTempAuth(0,authA)
    setTempAuth(1,authB)
    base_api = "https://9e98-158-140-163-210.ngrok.io/api/register/"
    

    while True:
        if isNewCard():
            data = readBlock(0,16,1)
            myobj = {'uid': toHexString(data)}
            print(myobj)
          
        sleep(0.5)