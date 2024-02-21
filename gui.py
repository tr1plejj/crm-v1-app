import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox, QPushButton
from PyQt5.QtGui import QPixmap
import crmapp
import telebot
from telebot import types
import requests
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)
tgk_chat_id = -1002112682526


class MainWindow(QMainWindow, crmapp.Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.icon_only_widget.hide()
        self.stackedWidget.setCurrentIndex(0)
        self.load_all_data()
        self.send_product_btn.clicked.connect(self.message_in_channel)
        self.upload_photo_btn.clicked.connect(self.add_image)
        self.send_current_offer_btn.clicked.connect(self.send_success_to_user)

    def add_image(self):
        pic = self.pic_path.text()
        self.label.setPixmap(QPixmap(pic))

    def on_product_btn1_toggled(self):
        self.stackedWidget.setCurrentIndex(1)

    def on_product_btn2_toggled(self):
        self.stackedWidget.setCurrentIndex(1)

    def on_offers_btn1_toggled(self):
        self.stackedWidget.setCurrentIndex(2)

    def on_offers_btn2_toggled(self):
        self.stackedWidget.setCurrentIndex(2)

    def on_user_btn_toggled(self):
        self.stackedWidget.setCurrentIndex(0)
        # if self.user_btn.isChecked():
        #     self.product_btn1.setChecked(False)
        #     self.product_btn1.setAutoExclusive(False)
        # else:
        #     self.product_btn1.setAutoExclusive(True)
    #     разобраться с кнопками и понять почему если нажимать на юзер то кнопка меняет свой цвет

    def load_all_data(self):
        try:
            all_data = requests.get('http://127.0.0.1:8000/get_offers_data').json()
            self.offers_table_widget.setRowCount(len(all_data))
            row = 0
            for i in all_data:
                self.offers_table_widget.setItem(row, 0, QTableWidgetItem(i['name']))
                self.offers_table_widget.setItem(row, 1, QTableWidgetItem(str(i['prod_id'])))
                self.offers_table_widget.setItem(row, 2, QTableWidgetItem(i['address']))
                self.offers_table_widget.setItem(row, 3, QTableWidgetItem(str(i['offer_id'])))
                row += 1
        except Exception as e:
            print('ошибка загрузки данных', e)

    @bot.message_handler()
    def send_success_to_user(self):
        try:
            cur_row = self.offers_table_widget.currentRow()
            select = QMessageBox.warning(self, 'Предупреждение', f'Вы уверены, что хотите отправить заказ?\n'
                                                                 f'Название: {self.offers_table_widget.item(cur_row, 0).text()}\n'
                                                                 f'ID товара: {self.offers_table_widget.item(cur_row, 1).text()}\n'
                                                                 f'Адрес доставки: {self.offers_table_widget.item(cur_row, 2).text()}\n'
                                                                 f'ID заказа: {self.offers_table_widget.item(cur_row, 3).text()}',
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if select == QMessageBox.StandardButton.Yes:
                id_offer = self.offers_table_widget.item(cur_row, 3).text()
                all_id = requests.get(f'http://127.0.0.1:8000/get_offer_and_return/{id_offer}').json()
                user_id = int(all_id)
                bot.send_message(chat_id=user_id, text=f'Ваш заказ под номером {id_offer} был отправлен')
                requests.delete(f'http://127.0.0.1:8000/delete_from_offers_db/{id_offer}')
                self.load_all_data()
            else:
                pass
        except Exception as e:
            print('error', e)

    @bot.message_handler()
    def message_in_channel(self):
        name = self.name.text()
        price = self.price.text()
        desc = self.description.text()
        pic = self.pic_path.text()
        try:
            prod_id = (
                requests.post(f'http://127.0.0.1:8000/put_in_db?name={name}&price={price}&description={desc}').json()
            )
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
            self.label.setPixmap(QPixmap(''))
            self.label.setStyleSheet("image: url(default_photo.png);")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
