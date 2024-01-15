# python -m PyQt5.uic.pyuic -x [FILENAME].ui -o [FILENAME].py
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import admin
import telebot

TOKEN = '6095405341:AAGVEIaNq0i6qdISCC2VtM3r3aExJN0jwQI'
bot = telebot.TeleBot(TOKEN)
class Admin(QtWidgets.QMainWindow, admin.Ui_Dialog):
    def __init__(self, parent=None):
        super(Admin, self).__init__(parent)
        self.setupUi(self)
        self.load_pic_button.clicked.connect(self.add_image)
        self.send_button.clicked.connect(self.message_in_channel)

    def add_image(self):
        pic = self.pic_path.text()
        self.label.setPixmap(QtGui.QPixmap(pic))
    @bot.message_handler()
    def message_in_channel(self, message):
        name = self.name.text()
        price = self.price.text()
        desc = self.description.text()
        pic = self.pic_path.text()
        img = open(pic, 'rb')
        bot.send_photo(-1002112682526, img)
        bot.send_message(-1002112682526, f'Товар: {name}\nЦена: {price}\nОписание: {desc}')
bot.polling()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    a = Admin()
    a.show()
    app.exec_()