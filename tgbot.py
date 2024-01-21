import telebot

from telebot import types
TOKEN = '6095405341:AAGVEIaNq0i6qdISCC2VtM3r3aExJN0jwQI'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def main_func(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    id_button = types.KeyboardButton('Сделать заказ')
    markup.add(id_button)
    bot.send_message(message.chat.id, text='hello', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Сделать заказ')
def answer_on_offer(message):
    bot.send_message(message.chat.id, 'Введите id товара', reply_markup=types.ReplyKeyboardRemove())

bot.polling()
