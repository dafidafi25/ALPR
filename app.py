import flask
from flask import  request,jsonify
from database import databaseConnector
import json
from queue import Queue, Empty
from threading import Thread
from time import sleep
from smartcard.System import readers
from smartcard.util import toHexString
from flask_cors import CORS,cross_origin

from rfid import init,readBlock,isNewCard
 
device = readers()
connection = device[0].createConnection()
connection.connect()

init()
authA = '00 00 00 00 00 00'
authB = 'FF FF FF FF FF FF'

CORS_ALLOW_ORIGIN="*,*"
CORS_EXPOSE_HEADERS="*,*"
CORS_ALLOW_HEADERS="content-type,*"

app = flask.Flask(__name__)
cors = CORS(app, origins=CORS_ALLOW_ORIGIN.split(","), allow_headers=CORS_ALLOW_HEADERS.split(",") , expose_headers= CORS_EXPOSE_HEADERS.split(","),   supports_credentials = True)
# app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'




database = databaseConnector(host="localhost",user="root",password="root",database="ANPR_RFID")


@app.route('/api/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/api/validate/plate_number/',methods = ['POST'])
def validate():
    content_type = request.headers.get('Content-Type')
    
    if (content_type == 'application/json'):
        plate_number = request.json['plate_number']
        result = database.validateDataByPlateNumber(plate_number=plate_number)
     
        
    return jsonify(result)


@app.route('/api/register/',methods = ['POST'])
def register():

    if isNewCard():
        data = readBlock(0,16,1)
        uid = toHexString(data)
        content_type = request.headers.get('Content-Type')

        if (content_type == 'application/json'):
            plate_number = request.json['plate_number']
            name = request.json['name']
            email = request.json['email']
            phone = request.json['phone']
            result =  {
                "uid" : uid,
                "plate_number": plate_number
            }
            database.insertData(uid=uid,plate_number=plate_number,name=name,email=email,phone=phone)
            return jsonify(result)
    else:
        return jsonify({
            "Message" : "New Card Not Detected"
        })
        
     
        
 




app.run(host="0.0.0.0",port=7000)

