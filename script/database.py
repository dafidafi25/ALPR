import mysql.connector
import json
###query###
INSERT_DATA = "INSERT INTO rfid (uid,plate_number,name,phone,email) VALUES (%s,%s,%s,%s,%s)"
GET_DATA_BY_UID = "SELECT * FROM rfid WHERE uid = %s"
GET_DATA_BY_PLATE_NUMBER = "SELECT * FROM rfid WHERE plate_number = %s"

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
    
    def insertData(self,uid,plate_number,name,phone,email):
        if self.validateDataByUid(uid) == False and self.validateDataByUid(plate_number) == False:
            val = (uid,plate_number,name,phone,email)
            self.controller.execute(INSERT_DATA,val)
            self.database.commit()
        else:
            print("Uid or plate number already registered")

    def validateDataByUid(self,uid):
        val = (uid,)

        self.controller.execute(GET_DATA_BY_UID,val)

        result = self.controller.fetchall()
        if len(result)>0:
            return {
                "id":result[0][0],
                "uid":result[0][1],
                "plate_number":result[0][2]
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
                "plate_number":result[0][2]
            }
        else:
            return False
        

if __name__=="__main__":
    database = databaseConnector(host="192.168.1.100",user="root",password="root",database="ANPR_RFID")
    uid_tester = "F7 D3 7B B5 EA 08 04 00 62 63 64 65 66 67 68 69"
    plate_number_tester = "w1232hg"

    # print(database.validateDataByUid(uid=uid_tester))
    # print(database.validateDataByPlateNumber(plate_number=plate_number_tester))