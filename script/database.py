import mysql.connector
import json
from datetime import datetime

###query###
INSERT_DATA = "INSERT INTO rfid (uid,plate_number,name,phone,email, status) VALUES (%s, %s, %s, %s, %s, %s)"
INSERT_LOG_DATA = "INSERT INTO rfid_log (user_id,status,waktu) VALUE (%s, %s, %s)"
GET_DATA_BY_UID = "SELECT * FROM rfid WHERE uid = %s"
GET_DATA_BY_PLATE_NUMBER = "SELECT * FROM rfid WHERE plate_number = %s"
GET_DATA_BY_ID = "SELECT * FROM rfid WHERE id = %s"
GET_ACCESS_LOG = "SELECT * FROM rfid_log ORDER BY id DESC"
UPDATE_DATA = "UPDATE rfid SET status = %s WHERE id = %s"
###query###


class databaseConnector:
    def __init__(self,host,user,password,database):
        self.database = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        self.controller =  self.database.cursor()
    
    def insertData(self,uid,plate_number,name,phone,email, status):
        if self.validateDataByUid(uid) == False and self.validateDataByUid(plate_number) == False:
            val = (uid,plate_number,name,phone,email, status)
            self.controller.execute(INSERT_DATA,val)
            self.database.commit()
        else:
            print("Uid or plate number already registered")
    
    def insertLogData(self,user_id,status):
        time = datetime.now()
        val = (user_id,status, time.strftime("%d/%m/%Y %H:%M:%S"))
        self.controller.execute(INSERT_LOG_DATA,val)
        self.database.commit()

        print(self.controller.rowcount, "record(s) affected")
    
    def updateStatus(self,status,id):
        
        val = (status,id)
        self.controller.execute(UPDATE_DATA,val)
        self.database.commit()

        print(self.controller.rowcount, "record(s) affected")



    def validateDataByUid(self,uid):
        val = (uid,)
        print(uid)

        self.controller.execute(GET_DATA_BY_UID,val)

        result = self.controller.fetchall()

        print(result)
        if len(result)>0:
            return {
                "id":result[0][0],
                "uid":result[0][1],
                "plate_number":result[0][2],
                "name":result[0][3],
                "phone":result[0][4],
                "email":result[0][5],
                "status":result[0][6],
            }
        else:
            return False

    def validateDataByPlateNumber(self,plate_number):
        val = (plate_number,)
        self.controller.execute(GET_DATA_BY_PLATE_NUMBER,val)
        result = self.controller.fetchall()

        if len(result)>0:
            return {
                "id":result[0][0],
                "uid":result[0][1],
                "plate_number":result[0][2],
                "name":result[0][3],
                "phone":result[0][4],
                "email":result[0][5],
                "status":result[0][6],
            }
        else:
            return False
    
    def getAccessLog(self):
        self.controller.execute(GET_ACCESS_LOG)
        results = self.controller.fetchall()
        row_headers=[x[0] for x in self.controller.description]
        json_data = []
        for result in results:
            json_data.append(dict(zip(row_headers,result)))
        self.controller =  self.database.cursor()
        return json_data
    
    def getRfidId(self,id):
        val = (int(id),)
        self.controller.execute(GET_DATA_BY_ID,val)
        results = self.controller.fetchall()
        row_headers=[x[0] for x in self.controller.description]
        json_data = []
        for result in results:
            json_data.append(dict(zip(row_headers,result)))
        self.controller =  self.database.cursor()
        return json_data

if __name__=="__main__":
    database = databaseConnector(host="localhost",user="admin",password="admin",database="ANPR_RFID")
    uid_tester = "F7 D3 7B B5 EA 08 04 00 62 63 64 65 66 67 68 69"
    plate_number_tester = "w1232hg"

    print(database.validateDataByUid(uid=uid_tester))
    # print(database.validateDataByPlateNumber(plate_number=plate_number_tester))