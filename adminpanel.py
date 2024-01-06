from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import admin


class Admin(QtWidgets.QMainWindow, admin.Ui_Dialog):
    def __init__(self, parent=None):
        super(Admin, self).__init__(parent)

        self.setupUi(self)
        self.send_button.clicked.connect(self.all_product)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    a = Admin()
    a.show()
    app.exec_()