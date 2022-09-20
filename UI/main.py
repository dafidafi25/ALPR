import sys

from PyQt5.QtWidgets import QMainWindow, QApplication


from Main_Window import Ui_MainWindow
from RegisterController import DialogRegister

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Admin GUI")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionRegister.triggered.connect(self.__show_register_form)
        self.register = None

    def __show_register_form(self):
        self.ui.worker.status = 1
        self.register = DialogRegister(self.ui.worker)
        self.register.start()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
