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
        self.send_button.clicked.connect(self.message_in_channel)

    @bot.message_handler()
    def message_in_channel(self, message):
        name = self.name.text()
        price = self.price.text()
        desc = self.description.text()
        bot.send_message(-1002112682526, f'Товар: {name}\nЦена: {price}\nОписание: {desc}')

if __name__ == '__main__':
    bot.polling()
    app = QtWidgets.QApplication(sys.argv)
    a = Admin()
    a.show()
    app.exec_()