import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QPixmap
import crmapp
from telebot import TeleBot, types
import requests
from os import getenv
# python -m PyQt5.uic.pyuic -x crmapp.ui -o crmapp.py
TOKEN = getenv('TOKEN')
tgk_chat_id = int(getenv('TGKCHATID'))
bot = TeleBot(TOKEN)
main_api_url = 'http://127.0.0.1:8000'


class MainWindow(QMainWindow, crmapp.Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.token = None
        self.headers = None
        self.setupUi(self)
        self.icon_only_widget.hide()
        self.stackedWidget.setCurrentIndex(0)
        self.product_btn1.setEnabled(False)
        self.product_btn2.setEnabled(False)
        self.offers_btn1.setEnabled(False)
        self.offers_btn2.setEnabled(False)
        self.user_btn.setEnabled(False)
        self.send_product_btn.clicked.connect(self.message_in_channel)
        self.upload_photo_btn.clicked.connect(self.add_image)
        self.send_current_offer_btn.clicked.connect(self.send_success_to_user)
        self.switch_login_btn.clicked.connect(self.switch_to_login_page)
        self.switch_register_btn.clicked.connect(self.switch_to_register_page)
        self.login_btn.clicked.connect(self.login_func)
        self.create_user_btn.clicked.connect(self.register_func)
        self.exit_btn1.clicked.connect(self.exit_func)
        self.exit_btn2.clicked.connect(self.exit_func)

    def switch_to_register_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_login_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def login_func(self):
        username = self.username_login.text()
        password = self.password_login.text()
        data = {'username': username, 'password': password}
        token_status = requests.post(url=f'{main_api_url}/api/auth/token/login', data=data)
        if token_status.status_code == 200:
            self.token = token_status.json().get('auth_token')
            self.headers = {'Authorization': f'Token {self.token}'}
            self.stackedWidget.setCurrentIndex(2)
            self.product_btn1.setEnabled(True)
            self.product_btn2.setEnabled(True)
            self.offers_btn1.setEnabled(True)
            self.offers_btn2.setEnabled(True)
            self.user_btn.setEnabled(True)
            self.load_all_data()
        else:
            print(token_status.text)

    def register_func(self):
        email = self.email.text()
        username = self.username_register.text()
        password = self.password_register.text()
        data = {'email': email, 'username': username, 'password': password}
        user_status = requests.post(url=f'{main_api_url}/api/auth/users/', data=data)
        if user_status.status_code == 201:
            self.stackedWidget.setCurrentIndex(0)
        else:
            print(user_status.text)

    def add_image(self):
        pic = self.pic_path.text()
        self.label.setPixmap(QPixmap(pic))

    def on_product_btn1_toggled(self):
        self.stackedWidget.setCurrentIndex(3)

    def on_product_btn2_toggled(self):
        self.stackedWidget.setCurrentIndex(3)

    def on_offers_btn1_toggled(self):
        self.stackedWidget.setCurrentIndex(4)

    def on_offers_btn2_toggled(self):
        self.stackedWidget.setCurrentIndex(4)

    def on_user_btn_toggled(self):
        self.stackedWidget.setCurrentIndex(2)

    def load_all_data(self):
        try:
            all_data = requests.get(f'{main_api_url}/api/orders/list/', headers=self.headers).json()
            self.offers_table_widget.setRowCount(len(all_data))
            row = 0
            for i in all_data:
                product = requests.get(url=f'{main_api_url}/api/product/get/{i.get('product')}', headers=self.headers).json()
                self.offers_table_widget.setItem(row, 0, QTableWidgetItem(product.get('title')))
                self.offers_table_widget.setItem(row, 1, QTableWidgetItem(str(i.get('product'))))
                self.offers_table_widget.setItem(row, 2, QTableWidgetItem(i.get('address')))
                self.offers_table_widget.setItem(row, 3, QTableWidgetItem(str(i.get('id'))))
                row += 1
        except Exception as e:
            print('ошибка загрузки данных', e)

    @bot.message_handler()
    def send_success_to_user(self):
        try:
            cur_row = self.offers_table_widget.currentRow()
            # либо сделать тут вывод названия товара, либо оставить его в цикле
            select = QMessageBox.warning(self, 'Предупреждение', f'Вы уверены, что хотите отправить заказ?\n'
                                                                 f'Название продукта: {self.offers_table_widget.item(cur_row, 0).text()}\n'
                                                                 f'ID товара: {self.offers_table_widget.item(cur_row, 1).text()}\n'
                                                                 f'Адрес доставки: {self.offers_table_widget.item(cur_row, 2).text()}\n'
                                                                 f'ID заказа: {self.offers_table_widget.item(cur_row, 3).text()}',
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if select == QMessageBox.StandardButton.Yes:
                id_offer = self.offers_table_widget.item(cur_row, 3).text()
                offer_data = requests.get(f'{main_api_url}/api/order/{id_offer}', headers=self.headers).json()
                user_id = offer_data.get('buyer_id')
                bot.send_message(chat_id=user_id, text=f'Ваш заказ под номером {id_offer} был отправлен')
                requests.delete(f'{main_api_url}/api/order/{id_offer}', headers=self.headers)
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
        data = {'title': name, 'description': desc, 'price': price}
        try:
            img = open(pic, 'rb')
            prod_id = requests.post(f'{main_api_url}/api/products/', headers=self.headers, data=data).json().get('id')
            markup = types.InlineKeyboardMarkup()
            offer_button = types.InlineKeyboardButton(text='Заказать', url='t.me/ReOrSellerBot')
            markup.add(offer_button)
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

    def exit_func(self):
        requests.post(url=f'{main_api_url}/api/auth/token/logout', headers=self.headers)
        sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
