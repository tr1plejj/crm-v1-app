# python -m PyQt5.uic.pyuic -x admin.ui -o admin.py
# python -m PyQt5.uic.pyuic -x offers.ui -o offers.py
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import admin
# from config import user, host, password, db_name
# from config import add_in_db
import telebot
from telebot import types
import requests

import offers

TOKEN = '6095405341:AAGVEIaNq0i6qdISCC2VtM3r3aExJN0jwQI'
bot = telebot.TeleBot(TOKEN)
tgk_chat_id = -1002112682526


class AdminSend(QtWidgets.QMainWindow, admin.Ui_Dialog):
    def __init__(self, parent=None):
        super(AdminSend, self).__init__(parent)
        self.setupUi(self)
        self.load_pic_button.clicked.connect(self.add_image)
        self.send_button.clicked.connect(self.message_in_channel)
        self.forward_button.clicked.connect(self.gotoOffers)

    def gotoOffers(self):
        widget.setCurrentWidget(admin_offers)

    def add_image(self):
        pic = self.pic_path.text()
        self.label.setPixmap(QtGui.QPixmap(pic))

    @bot.message_handler()
    def message_in_channel(self, message):
        name = self.name.text()
        price = self.price.text()
        desc = self.description.text()
        pic = self.pic_path.text()
        try:
            prod_id = requests.get(f'http://127.0.0.1:8000/put_in_db/{name}/{price}/{desc}').json()
            prod_id = prod_id[0]
            markup = types.InlineKeyboardMarkup()
            offer_button = types.InlineKeyboardButton(text='Offer', url='t.me/ReOrSellerBot')
            markup.add(offer_button)
            img = open(pic, 'rb')
            bot.send_photo(tgk_chat_id,
                           photo=img,
                           caption=f'Товар: {name}\nЦена: {price}\nОписание: {desc}\nID товара: {prod_id}',
                           reply_markup=markup)
        except:
            print('неверно введены какие-либо данные')

        finally:
            self.name.clear()
            self.price.clear()
            self.description.clear()
            self.pic_path.clear()


class AdminOffers(QtWidgets.QMainWindow, offers.Ui_Dialog):
    def __init__(self, parent=None):
        super(AdminOffers, self).__init__(parent)
        self.setupUi(self)
        self.back_button.clicked.connect(self.gotoPanel)

    def gotoPanel(self):
        widget.setCurrentWidget(admin_send)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    admin_send = AdminSend()
    admin_offers = AdminOffers()
    widget.addWidget(admin_send)
    widget.addWidget(admin_offers)
    widget.setFixedSize(700, 650)
    widget.show()
    app.exec_()
