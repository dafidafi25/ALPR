import sys

from PyQt5.QtWidgets import QMainWindow, QApplication


from Main_Window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        print('wawa')
        super(MainWindow, self).__init__()
        self.setWindowTitle("Admin GUI")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
