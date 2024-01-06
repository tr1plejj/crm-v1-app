#6095405341:AAGVEIaNq0i6qdISCC2VtM3r3aExJN0jwQI
#https://api.telegram.org/bot6095405341:AAGVEIaNq0i6qdISCC2VtM3r3aExJN0jwQI/getChat?chat_id=@fastsellandresell
import telebot
from adminpanel import Admin
class All(Admin):
    def all_product(self):
        name = self.name.text()
        price = self.price.text()
        desc = self.description.text()
        @bot.message_handler(commands=['send'])
        def message_in_channel(message):
            bot.send_message(-1002112682526, name)

TOKEN = '6095405341:AAGVEIaNq0i6qdISCC2VtM3r3aExJN0jwQI'

bot = telebot.TeleBot(TOKEN)

bot.infinity_polling()