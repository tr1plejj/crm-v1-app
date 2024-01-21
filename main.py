# python -m PyQt5.uic.pyuic -x admin.ui -o admin.py
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import admin
import telebot
from telebot import types

TOKEN = '6095405341:AAGVEIaNq0i6qdISCC2VtM3r3aExJN0jwQI'
bot = telebot.TeleBot(TOKEN)
tgk_chat_id = -1002112682526
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
        markup = types.InlineKeyboardMarkup()
        offer_button = types.InlineKeyboardButton(text='Offer', url='t.me/ReOrSellerBot')
        markup.add(offer_button)
        img = open(pic, 'rb')
        bot.send_photo(tgk_chat_id,
                       photo=img,
                       caption=f'Товар: {name}\nЦена: {price}\nОписание: {desc}',
                       reply_markup=markup)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    a = Admin()
    a.show()
    app.exec_()