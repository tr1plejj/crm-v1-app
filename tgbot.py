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
    bot.send_message(message.chat.id, text='Нажмите кнопку "Сделать заказ" для продолжения', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Сделать заказ')
def answer_on_offer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    no = types.KeyboardButton('Отмена')
    markup.add(no)
    bot.send_message(message.chat.id, 'Введите id товара', reply_markup=markup)
    bot.register_next_step_handler(message, return_db_data)


def return_db_data(message):
    try:
        if message.text == 'Отмена':
            bot.message_handler(main_func(message))
            return
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        yes = types.KeyboardButton('Заказать')
        no = types.KeyboardButton('Отмена')
        markup.row(yes, no)
        data = requests.get(f'http://127.0.0.1:8000/get_from_db/{message.text}').json()
        name = data[0][0]
        price = data[0][1]
        desc = data[0][2]
        bot.send_message(message.chat.id, f'Название товара: {name}\nЦена: {price}\nОписание: {desc}')
        bot.send_message(message.chat.id, 'Оформить заказ?', reply_markup=markup)
        bot.register_next_step_handler(message, get_address)
    except:
        bot.send_message(message.chat.id, 'Такого товара не существует')
        bot.register_next_step_handler(message, return_db_data)

def get_address(message):
    if message.text == 'Заказать':
        bot.send_message(message.chat.id, 'you pressed yes')
    if message.text == 'Отмена':
        bot.message_handler(main_func(message))


bot.polling()
