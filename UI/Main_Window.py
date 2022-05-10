from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

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
        self.Nama = QLabel(self.horizontalLayoutWidget_2)
        self.Nama.setObjectName(u"Nama")
        self.Nama.setAlignment(Qt.AlignCenter)

        self.left_layout.setWidget(1, QFormLayout.LabelRole, self.Nama)

        self.Email = QLabel(self.horizontalLayoutWidget_2)
        self.Email.setObjectName(u"Email")
        self.Email.setAlignment(Qt.AlignCenter)
        self.Email.setWordWrap(False)

        self.left_layout.setWidget(0, QFormLayout.LabelRole, self.Email)


        self.TableLayout.addLayout(self.left_layout)

        self.right_layout = QFormLayout()
        self.right_layout.setObjectName(u"right_layout")
        self.Registered_plate = QLabel(self.horizontalLayoutWidget_2)
        self.Registered_plate.setObjectName(u"Registered_plate")
        self.Registered_plate.setAlignment(Qt.AlignCenter)

        self.right_layout.setWidget(1, QFormLayout.LabelRole, self.Registered_plate)

        self.Phone = QLabel(self.horizontalLayoutWidget_2)
        self.Phone.setObjectName(u"Phone")
        self.Phone.setAlignment(Qt.AlignCenter)

        self.right_layout.setWidget(0, QFormLayout.LabelRole, self.Phone)


        self.TableLayout.addLayout(self.right_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Gambar1.setText(QCoreApplication.translate("MainWindow", u"gambar1", None))
        self.ket_gambar2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.gambar2.setText(QCoreApplication.translate("MainWindow", u"gambar2", None))
        self.ket_gambar3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.gambar3.setText(QCoreApplication.translate("MainWindow", u"gambar2", None))
        self.Nama.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Email.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Registered_plate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Phone.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))