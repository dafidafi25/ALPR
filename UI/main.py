import sys

# from PySide6.QtGui import QIcon
# from PySide6.QtCore import QTimer
# from PySide6.QtWidgets import QApplication, QMainWindow
from Main_Window import Ui_MainWindow
from PySide2.QtWidgets import QApplication,QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Admin GUI")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
