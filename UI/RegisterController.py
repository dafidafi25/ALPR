from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore
from RegisteForm import Ui_Dialog
import sys
import requests
import json
sys.path.insert(1, '/home/rio/work/tugas_akhir/ALPR/script')
import rfid #type: ignore
url = 'http://localhost:7000/api'

class DialogRegister(QDialog):
    def __init__(self, worker):
        super().__init__()
        self.worker = worker
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.__initialize_button()
    
    def __initialize_button(self):
        self.ui.btn_register_2.clicked.connect(self.__register)
        self.ui.btn_scan_2.clicked.connect(self.__scan)
        pass

    def closeEvent(self, evnt):
        self.worker.status = 0
     

    def __register(self):
        email = self.ui.input_email_2.text()
        phone = self.ui.input_phone_2.text()
        plate_number = self.ui.input_saldo_2.text()
        uid = self.ui.input_uid_2.text()
        name = self.ui.input_username_2.text()
        
        data = requests.post(url+"/register/",json={
                            "uid": uid,
                            "phone": phone,
                            "email" : email,
                            "plate_number": plate_number,
                            "name" : name,
                            "status" : 0
                        }).json()

    def __scan(self):
        if rfid.isNewCard():
            data = rfid.readBlock(0,16,1)
            data = rfid.toHexString(data)
            self.ui.input_uid_2.setText(data)
       
    def start(self):
        self.exec_()

    def __result_change_price():
        pass
