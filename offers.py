# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'offers.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(691, 597)
        Dialog.setFocusPolicy(QtCore.Qt.NoFocus)
        self.back_button = QtWidgets.QPushButton(Dialog)
        self.back_button.setGeometry(QtCore.QRect(60, 510, 75, 23))
        self.back_button.setObjectName("back_button")
        self.offers_data = QtWidgets.QTableWidget(Dialog)
        self.offers_data.setGeometry(QtCore.QRect(40, 40, 560, 311))
        self.offers_data.setFocusPolicy(QtCore.Qt.NoFocus)
        self.offers_data.setAutoFillBackground(False)
        self.offers_data.setStyleSheet("QTableWidget {\n"
"    border-radius: 3px;\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    border: none;\n"
"    border-bottom: 1px solid #000;\n"
"    text-align: left;\n"
"    padding: 3px 5px;\n"
"}\n"
"\n"
"QTableWidget::Item {\n"
"    padding-left: 3px;\n"
"    border-bottom: 1px solid #000;\n"
"}\n"
"")
        self.offers_data.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.offers_data.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.offers_data.setLineWidth(1)
        self.offers_data.setAutoScroll(True)
        self.offers_data.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.offers_data.setDragEnabled(False)
        self.offers_data.setAlternatingRowColors(False)
        self.offers_data.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.offers_data.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.offers_data.setTextElideMode(QtCore.Qt.ElideNone)
        self.offers_data.setShowGrid(False)
        self.offers_data.setGridStyle(QtCore.Qt.SolidLine)
        self.offers_data.setWordWrap(True)
        self.offers_data.setCornerButtonEnabled(True)
        self.offers_data.setObjectName("offers_data")
        self.offers_data.setColumnCount(4)
        self.offers_data.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.offers_data.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.offers_data.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.offers_data.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.offers_data.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.offers_data.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.offers_data.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.offers_data.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.offers_data.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.offers_data.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.offers_data.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.offers_data.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.offers_data.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.offers_data.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.offers_data.setItem(1, 3, item)
        self.offers_data.horizontalHeader().setVisible(True)
        self.offers_data.horizontalHeader().setCascadingSectionResizes(True)
        self.offers_data.horizontalHeader().setDefaultSectionSize(130)
        self.offers_data.horizontalHeader().setHighlightSections(True)
        self.offers_data.horizontalHeader().setMinimumSectionSize(25)
        self.offers_data.horizontalHeader().setSortIndicatorShown(False)
        self.offers_data.horizontalHeader().setStretchLastSection(True)
        self.offers_data.verticalHeader().setVisible(False)
        self.offers_data.verticalHeader().setCascadingSectionResizes(False)
        self.offers_data.verticalHeader().setDefaultSectionSize(35)
        self.offers_data.verticalHeader().setMinimumSectionSize(20)
        self.offers_data.verticalHeader().setSortIndicatorShown(False)
        self.offers_data.verticalHeader().setStretchLastSection(False)
        self.send_off_btn = QtWidgets.QPushButton(Dialog)
        self.send_off_btn.setGeometry(QtCore.QRect(460, 360, 141, 41))
        self.send_off_btn.setObjectName("send_off_btn")
        self.refresh_btn = QtWidgets.QPushButton(Dialog)
        self.refresh_btn.setGeometry(QtCore.QRect(610, 40, 51, 41))
        self.refresh_btn.setObjectName("refresh_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.back_button.setText(_translate("Dialog", "back"))
        self.offers_data.setSortingEnabled(False)
        item = self.offers_data.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Новая строка"))
        item = self.offers_data.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "Новая строка"))
        item = self.offers_data.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Название"))
        item = self.offers_data.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "ID"))
        item = self.offers_data.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Адрес доставки"))
        item = self.offers_data.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "ID заказа"))
        __sortingEnabled = self.offers_data.isSortingEnabled()
        self.offers_data.setSortingEnabled(False)
        item = self.offers_data.item(0, 0)
        item.setText(_translate("Dialog", "2"))
        item = self.offers_data.item(0, 1)
        item.setText(_translate("Dialog", "2"))
        item = self.offers_data.item(0, 2)
        item.setText(_translate("Dialog", "2"))
        item = self.offers_data.item(0, 3)
        item.setText(_translate("Dialog", "2"))
        item = self.offers_data.item(1, 0)
        item.setText(_translate("Dialog", "1"))
        item = self.offers_data.item(1, 1)
        item.setText(_translate("Dialog", "1"))
        item = self.offers_data.item(1, 2)
        item.setText(_translate("Dialog", "1"))
        item = self.offers_data.item(1, 3)
        item.setText(_translate("Dialog", "1"))
        self.offers_data.setSortingEnabled(__sortingEnabled)
        self.send_off_btn.setText(_translate("Dialog", "Отправить заказ"))
        self.refresh_btn.setText(_translate("Dialog", "🔄"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
