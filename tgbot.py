import telebot
from config import take_from_db
import requests

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

@bot.message_handler()
def return_db_data(message):
    data = requests.get(f'http://127.0.0.1:8000/{message.text}').json()
    name = data[0][0]
    price = data[0][1]
    desc = data[0][2]
    bot.send_message(message.chat.id, f'{name} {price} {desc}')

bot.polling()
