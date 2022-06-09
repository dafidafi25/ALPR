# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from cgitb import grey
from time import sleep
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QThread)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

import requests
import re

from PySide2 import QtGui,QtCore
import cv2
# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/home/pi/work/tugas_akhir/ALPR/script')
import rfid #type: ignore
import licenese_plate_6 #type: ignore
from database import databaseConnector #type: ignore
from hikvision import isapiClient #type: ignore

from smartcard.util import toHexString


class WorkerThread(QThread):
    update_reader = QtCore.Signal(object,object,object)
    update_user = QtCore.Signal(dict)
   
    rfid.init()
    def run(self):
        self.gate = 0
        self.cnt = 0
        ip = "192.168.2.64"
        port = "80"
        host = 'http://'+ip + ':'+ port
        url = 'http://192.168.1.130:7000/api'
        self.cam = isapiClient(host, 'admin', '-arngnennscfrer2')
        while True:
            if rfid.isNewCard() and self.gate == 0:
                try:
                    print("tes")
                    data_hex = rfid.readBlock(0,16,1)
                    data_hex = toHexString(data_hex)

                    data = requests.post(url+"/validate/uid/",json={
                        "uid": data_hex
                    }).json()

                    # self.cctv_img = self.requestPicture()
                    self.cctv_img = cv2.imread("/home/pi/work/tugas_akhir/ALPR/images/rio/35.jpeg")
                   
                    img,cropped_thresh,cropped, detected_string = licenese_plate_6.detect_plate(self.cctv_img )
                    detected_string = re.findall(r'\(?([0-9A-Za-z]+)\)?', detected_string)
                    regex = ""
                    cnt = 0
                    print(detected_string)
                    for text in detected_string:
                        regex += text
                        if cnt != len(detected_string)-1:
                            regex += " "
                        cnt+=1
                    self.update_reader.emit(img,cropped_thresh,cropped)
        
                    # self.update_reader.emit(img,cropped_thresh,cropped)
                    valid = requests.post(url+"/validate/plate_number/",json={
                        "plate_number": regex
                    }).json()

                    assert valid != False, "Plate Number not Registered"
                    if data['status'] == None:
                        data['status'] = 0
                
             
                    requests.post(url+"/insert/log", json = {
                        "user_id": int(data['id']),
                        "status": int(data['status'])
                    })
           
                    requests.post(url+"/update/" + str(data['id']) , json = {
                        "status": 1 if data['status'] == 0  else 0 
                    })
    
                    self.update_user.emit(data)
                    print("berhasil")

                    
                    self.openGate()
                except:
                    # self.update_reader.emit(self.cctv_img,self.cctv_img,self.cctv_img)
                    print("error")
            elif self.gate == 1:
                self.counting()
                if self.cnt == 5:
                    self.closeGate()
                    self.reset()
                    
            sleep(1)
    
    def openGate(self):
        self.gate = 1

    def closeGate(self):
        self.gate = 0
    
    def counting(self):
        self.cnt += 1
    
    def reset(self):
        self.gate = 0
        self.cnt = 0
    
    def requestPicture(self):
        img = self.cam.pictureRequest()
        return img

class WorkerThread2(QThread):
    def run(self):
        import app #type: ignore
        

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 771, 401))
        grey = QPixmap(500,401)
        grey.fill(QColor('darkgray'))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Gambar1 = QLabel(self.horizontalLayoutWidget)
        self.Gambar1.setObjectName(u"Gambar1")

        self.horizontalLayout.addWidget(self.Gambar1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ket_gambar2 = QLabel(self.horizontalLayoutWidget)
        self.ket_gambar2.setObjectName(u"ket_gambar2")
        self.ket_gambar2.setMaximumSize(QSize(389, 54))
        self.ket_gambar2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.ket_gambar2)

        self.gambar2 = QLabel(self.horizontalLayoutWidget)
        self.gambar2.setObjectName(u"gambar2")
        self.gambar2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.gambar2)

        self.ket_gambar3 = QLabel(self.horizontalLayoutWidget)
        self.ket_gambar3.setObjectName(u"ket_gambar3")
        self.ket_gambar3.setMaximumSize(QSize(389, 54))
        self.ket_gambar3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.ket_gambar3)

        self.gambar3 = QLabel(self.horizontalLayoutWidget)
        self.gambar3.setObjectName(u"gambar3")
        self.gambar3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.gambar3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 430, 771, 121))
        self.TableLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.TableLayout.setObjectName(u"TableLayout")
        self.TableLayout.setContentsMargins(0, 0, 0, 0)
        self.left_layout = QFormLayout()
        self.left_layout.setObjectName(u"left_layout")
        self.left_layout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Nama = QLabel(self.horizontalLayoutWidget_2)
        self.Nama.setObjectName(u"Nama")
        self.Nama.setAlignment(Qt.AlignCenter)

        self.left_layout.setWidget(0, QFormLayout.LabelRole, self.Nama)

        self.Email = QLabel(self.horizontalLayoutWidget_2)
        self.Email.setObjectName(u"Email")
        self.Email.setAlignment(Qt.AlignCenter)
        self.Email.setWordWrap(False)

        self.left_layout.setWidget(2, QFormLayout.LabelRole, self.Email)
        
        self.Status = QLabel(self.horizontalLayoutWidget_2)
        self.Status.setObjectName(u"Status")
        self.Status.setAlignment(Qt.AlignCenter)
        self.Status.setWordWrap(False)

        self.left_layout.setWidget(1, QFormLayout.LabelRole, self.Status)


        self.TableLayout.addLayout(self.left_layout)

        self.right_layout = QFormLayout()
        self.right_layout.setObjectName(u"right_layout")
        self.right_layout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Registered_plate = QLabel(self.horizontalLayoutWidget_2)
        self.Registered_plate.setObjectName(u"Registered_plate")
        self.Registered_plate.setAlignment(Qt.AlignCenter)

        self.right_layout.setWidget(1, QFormLayout.LabelRole, self.Registered_plate)

        self.Phone = QLabel(self.horizontalLayoutWidget_2)
        self.Phone.setObjectName(u"Phone")
        self.Phone.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.right_layout.setWidget(0, QFormLayout.LabelRole, self.Phone)


        self.TableLayout.addLayout(self.right_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.Gambar1.setPixmap(grey)
        self.gambar2.setPixmap(grey)
        self.gambar3.setPixmap(grey)

        self.worker = WorkerThread()
        self.worker.start()
        self.worker.update_reader.connect(self.handlerfid)
        self.worker.update_user.connect(self.handleUpdateText)

        self.worker2 = WorkerThread2()
        self.worker2.start()
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Gambar1.setText("")
        self.ket_gambar2.setText(QCoreApplication.translate("MainWindow", u"Pelat Nomor", None))
        self.gambar2.setText("")
        self.ket_gambar3.setText(QCoreApplication.translate("MainWindow", u"Pelat Nomor Olahan", None))
        self.gambar3.setText("")
        self.Nama.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.Email.setText(QCoreApplication.translate("MainWindow", u"Nama", None))
        self.Registered_plate.setText(QCoreApplication.translate("MainWindow", u"Pelat Nomor", None))
        self.Phone.setText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.Status.setText(QCoreApplication.translate("MainWindow", u"Status", None))
    # retranslateUi
    
    def convert_cv_qt(self, img, widht, height):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(widht, height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
    
    def handlerfid(self,img,cropped_thresh,cropped):
        self.setImage1(img,cropped_thresh,cropped)
    
    def handleUpdateText(self,data):
        plate_number = data['plate_number']
        name = data['name']
        phone = data['phone']
        email = data['email']
        status = data['status']
        self.Status.setText("Masuk" if status == 0 else "Keluar")
        self.Nama.setText(name)
        self.Phone.setText(phone)
        self.Registered_plate.setText(plate_number)
        self.Email.setText(email)

    
    def setImage1(self,img,cropped_thresh,cropped):
        qt_img = self.convert_cv_qt(img,382,399)
        self.Gambar1.setPixmap(qt_img)
        qt_img = self.convert_cv_qt(cropped,379,136)
        self.gambar2.setPixmap(qt_img)
        qt_img = self.convert_cv_qt(cropped_thresh,379,136)
        self.gambar3.setPixmap(qt_img)

