# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RegisteForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.layput_username_2 = QHBoxLayout()
        self.layput_username_2.setObjectName(u"layput_username_2")
        self.label_username_2 = QLabel(Dialog)
        self.label_username_2.setObjectName(u"label_username_2")

        self.layput_username_2.addWidget(self.label_username_2)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.layput_username_2.addWidget(self.label_7)

        self.input_username_2 = QLineEdit(Dialog)
        self.input_username_2.setObjectName(u"input_username_2")

        self.layput_username_2.addWidget(self.input_username_2)

        self.layput_username_2.setStretch(0, 2)
        self.layput_username_2.setStretch(1, 1)
        self.layput_username_2.setStretch(2, 9)

        self.verticalLayout.addLayout(self.layput_username_2)

        self.layout_email_2 = QHBoxLayout()
        self.layout_email_2.setObjectName(u"layout_email_2")
        self.label_email_2 = QLabel(Dialog)
        self.label_email_2.setObjectName(u"label_email_2")

        self.layout_email_2.addWidget(self.label_email_2)

        self.label_14 = QLabel(Dialog)
        self.label_14.setObjectName(u"label_14")

        self.layout_email_2.addWidget(self.label_14)

        self.input_email_2 = QLineEdit(Dialog)
        self.input_email_2.setObjectName(u"input_email_2")

        self.layout_email_2.addWidget(self.input_email_2)

        self.layout_email_2.setStretch(0, 2)
        self.layout_email_2.setStretch(1, 1)
        self.layout_email_2.setStretch(2, 9)

        self.verticalLayout.addLayout(self.layout_email_2)

        self.layout_phone_2 = QHBoxLayout()
        self.layout_phone_2.setObjectName(u"layout_phone_2")
        self.label_phone_2 = QLabel(Dialog)
        self.label_phone_2.setObjectName(u"label_phone_2")

        self.layout_phone_2.addWidget(self.label_phone_2)

        self.label_12 = QLabel(Dialog)
        self.label_12.setObjectName(u"label_12")

        self.layout_phone_2.addWidget(self.label_12)

        self.input_phone_2 = QLineEdit(Dialog)
        self.input_phone_2.setObjectName(u"input_phone_2")

        self.layout_phone_2.addWidget(self.input_phone_2)

        self.layout_phone_2.setStretch(0, 2)
        self.layout_phone_2.setStretch(1, 1)
        self.layout_phone_2.setStretch(2, 9)

        self.verticalLayout.addLayout(self.layout_phone_2)

        self.layout_saldo_2 = QHBoxLayout()
        self.layout_saldo_2.setObjectName(u"layout_saldo_2")
        self.label_saldo_2 = QLabel(Dialog)
        self.label_saldo_2.setObjectName(u"label_saldo_2")

        self.layout_saldo_2.addWidget(self.label_saldo_2)

        self.label_15 = QLabel(Dialog)
        self.label_15.setObjectName(u"label_15")

        self.layout_saldo_2.addWidget(self.label_15)

        self.input_saldo_2 = QLineEdit(Dialog)
        self.input_saldo_2.setObjectName(u"input_saldo_2")

        self.layout_saldo_2.addWidget(self.input_saldo_2)

        self.layout_saldo_2.setStretch(0, 2)
        self.layout_saldo_2.setStretch(1, 1)
        self.layout_saldo_2.setStretch(2, 9)

        self.verticalLayout.addLayout(self.layout_saldo_2)

        self.layou_uid_2 = QHBoxLayout()
        self.layou_uid_2.setObjectName(u"layou_uid_2")
        self.label_uid_2 = QLabel(Dialog)
        self.label_uid_2.setObjectName(u"label_uid_2")

        self.layou_uid_2.addWidget(self.label_uid_2)

        self.label_13 = QLabel(Dialog)
        self.label_13.setObjectName(u"label_13")

        self.layou_uid_2.addWidget(self.label_13)

        self.input_uid_2 = QLineEdit(Dialog)
        self.input_uid_2.setObjectName(u"input_uid_2")

        self.layou_uid_2.addWidget(self.input_uid_2)

        self.layou_uid_2.setStretch(0, 2)
        self.layou_uid_2.setStretch(1, 1)
        self.layou_uid_2.setStretch(2, 9)

        self.verticalLayout.addLayout(self.layou_uid_2)

        self.layout_action_2 = QHBoxLayout()
        self.layout_action_2.setObjectName(u"layout_action_2")
        self.btn_scan_2 = QPushButton(Dialog)
        self.btn_scan_2.setObjectName(u"btn_scan_2")

        self.layout_action_2.addWidget(self.btn_scan_2)

        self.btn_register_2 = QPushButton(Dialog)
        self.btn_register_2.setObjectName(u"btn_register_2")

        self.layout_action_2.addWidget(self.btn_register_2)


        self.verticalLayout.addLayout(self.layout_action_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Form Pendaftaran", None))
        self.label_username_2.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u":", None))
        self.label_email_2.setText(QCoreApplication.translate("Dialog", u"Email ", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u":", None))
        self.label_phone_2.setText(QCoreApplication.translate("Dialog", u"Phone", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u":", None))
        self.label_saldo_2.setText(QCoreApplication.translate("Dialog", u"Nopol", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u":", None))
        self.label_uid_2.setText(QCoreApplication.translate("Dialog", u"UID", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u":", None))
        self.btn_scan_2.setText(QCoreApplication.translate("Dialog", u"Scan", None))
        self.btn_register_2.setText(QCoreApplication.translate("Dialog", u"Daftar", None))
    # retranslateUi

