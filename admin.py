# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(568, 630)
        self.name = QtWidgets.QLineEdit(Dialog)
        self.name.setGeometry(QtCore.QRect(170, 370, 181, 41))
        self.name.setObjectName("name")
        self.price = QtWidgets.QLineEdit(Dialog)
        self.price.setGeometry(QtCore.QRect(170, 430, 181, 41))
        self.price.setObjectName("price")
        self.description = QtWidgets.QLineEdit(Dialog)
        self.description.setGeometry(QtCore.QRect(170, 490, 181, 71))
        self.description.setObjectName("description")
        self.send_button = QtWidgets.QPushButton(Dialog)
        self.send_button.setGeometry(QtCore.QRect(200, 580, 131, 31))
        self.send_button.setObjectName("send_button")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 10, 281, 221))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pic.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pic_path = QtWidgets.QLineEdit(Dialog)
        self.pic_path.setGeometry(QtCore.QRect(170, 250, 181, 31))
        self.pic_path.setObjectName("pic_path")
        self.load_pic_button = QtWidgets.QPushButton(Dialog)
        self.load_pic_button.setGeometry(QtCore.QRect(230, 310, 61, 20))
        self.load_pic_button.setObjectName("load_pic_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.send_button.setText(_translate("Dialog", "send"))
        self.load_pic_button.setText(_translate("Dialog", "load"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
