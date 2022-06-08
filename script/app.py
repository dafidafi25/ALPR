import flask
from flask import request, jsonify
from database import databaseConnector
import json
from queue import Queue, Empty
from threading import Thread
from time import sleep
from smartcard.System import readers
from smartcard.util import toHexString
from flask_cors import CORS,cross_origin
# from flask_mysqldb import MySQL

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
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'rfid_log'

# mysql = MySQL(app)

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

@app.route('/api/validate/uid/',methods = ['POST'])
def validateByUid():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        uid = request.json['uid']
        print(uid)
        result = database.validateDataByUid(uid)
     
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

@app.route('/api/rfid/get', methods=['GET'])
def getData():
    rows = database.getAccessLog()
    return jsonify(rows)     

@app.route('/api/insert/log',methods = ['POST'])
def insertLog():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        user_id = request.json['user_id']
        status = request.json['status']
        print(user_id,status)
        result = database.insertLogData(user_id,status)
        return jsonify(result)

@app.route('/api/update/<int:id>',methods = ['POST'])
def updateStatus(id):
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        status = request.json['status']
        result = database.updateStatus(status,id)
        return jsonify(result)

@app.route('/api/rfid/get/<int:id>', methods=['GET'])
def getDataById(id):
    rows = database.getRfidId(id)
    return jsonify(rows)
        
 
app.run(host="0.0.0.0",port=7000)

