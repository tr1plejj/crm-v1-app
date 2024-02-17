# python -m PyQt5.uic.pyuic -x admin.ui -o admin.py
# python -m PyQt5.uic.pyuic -x offers.ui -o offers.py
# python -m PyQt5.uic.pyuic -x crmapp.ui -o crmapp.py
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QMessageBox, QMainWindow
import sys
import admin
import telebot
from telebot import types
import requests
import offers

TOKEN = '6095405341:AAGVEIaNq0i6qdISCC2VtM3r3aExJN0jwQI'
bot = telebot.TeleBot(TOKEN)
tgk_chat_id = -1002112682526


class AdminSend(QMainWindow, admin.Ui_Dialog):
    def __init__(self, parent=None):
        super(AdminSend, self).__init__(parent)
        self.setupUi(self)
        self.load_pic_button.clicked.connect(self.add_image)
        self.send_button.clicked.connect(self.message_in_channel)
        self.forward_button.clicked.connect(self.goto_offers)

    @staticmethod
    def goto_offers():
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
            prod_id = (requests.post(f'http://127.0.0.1:8000/put_in_db?name={name}&price={price}&description={desc}').json())
            prod_id = int(prod_id)
            markup = types.InlineKeyboardMarkup()
            offer_button = types.InlineKeyboardButton(text='Offer', url='t.me/ReOrSellerBot')
            markup.add(offer_button)
            img = open(pic, 'rb')
            bot.send_photo(tgk_chat_id,
                           photo=img,
                           caption=f'Товар: {name}\nЦена: {price}\nОписание: {desc}\nID товара: {prod_id}',
                           reply_markup=markup)
        except Exception as e:
            print('неверно введены какие-либо данные', e)

        finally:
            self.name.clear()
            self.price.clear()
            self.description.clear()
            self.pic_path.clear()


class AdminOffers(QMainWindow, offers.Ui_Dialog):
    def __init__(self, parent=None):
        super(AdminOffers, self).__init__(parent)
        self.setupUi(self)
        self.back_button.clicked.connect(self.goto_panel)
        self.load_all_data()
        self.send_off_btn.clicked.connect(self.send_success_to_user)
        self.offers_data.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.refresh_btn.clicked.connect(self.load_all_data)
        
    @staticmethod
    def goto_panel():
        widget.setCurrentWidget(admin_send)

    def load_all_data(self):
        try:
            all_data = requests.get('http://127.0.0.1:8000/get_offers_data').json()
            self.offers_data.setRowCount(len(all_data))
            row = 0
            for i in all_data:
                self.offers_data.setItem(row, 0, QtWidgets.QTableWidgetItem(i['name']))
                self.offers_data.setItem(row, 1, QtWidgets.QTableWidgetItem(str(i['prod_id'])))
                self.offers_data.setItem(row, 2, QtWidgets.QTableWidgetItem(i['address']))
                self.offers_data.setItem(row, 3, QtWidgets.QTableWidgetItem(str(i['offer_id'])))
                row += 1
        except Exception as e:
            print('ошибка загрузки данных', e)

    @bot.message_handler()
    def send_success_to_user(self, message):
        try:
            cur_row = self.offers_data.currentRow()
            select = QMessageBox.warning(self, 'Предупреждение', f'Вы уверены, что хотите отправить заказ?\n'
                                                                 f'Название: {self.offers_data.item(cur_row, 0).text()}\n'
                                                                 f'ID товара: {self.offers_data.item(cur_row, 1).text()}\n'
                                                                 f'Адрес доставки: {self.offers_data.item(cur_row, 2).text()}\n'
                                                                 f'ID заказа: {self.offers_data.item(cur_row, 3).text()}',
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if select == QMessageBox.StandardButton.Yes:
                id_offer = self.offers_data.item(cur_row, 3).text()
                all_id = requests.get(f'http://127.0.0.1:8000/get_offer_and_return/{id_offer}').json()
                user_id = int(all_id[0])
                bot.send_message(chat_id=user_id, text=f'Ваш заказ под номером {id_offer} был отправлен')
                requests.delete(f'http://127.0.0.1:8000/delete_from_offers_db/{id_offer}')
                self.load_all_data()
            else:
                pass
        except Exception as e:
            print('error', e)


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

#разобраться с выделением строки + (НУ ПОЧТИ) удалить сразу данные из таблицы при отправке