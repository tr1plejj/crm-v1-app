import telebot
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
    print(message.text, 'start')


@bot.message_handler(func=lambda message: message.text == 'Сделать заказ')
def answer_on_offer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    no = types.KeyboardButton('Отмена')
    markup.add(no)
    bot.send_message(message.chat.id, 'Введите id товара', reply_markup=markup)
    bot.register_next_step_handler(message, return_db_data)
    print(message.text, 'answer on offer')


def return_db_data(message):
    global prod_id
    try:
        if message.text == 'Отмена':
            bot.message_handler(main_func(message))
            return
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        yes = types.KeyboardButton('Заказать')
        no = types.KeyboardButton('Отмена')
        markup.row(yes, no)
        prod_id = message.text
        data = requests.get(f'http://127.0.0.1:8000/take_from_db/{prod_id}').json()
        name = data[0][0]
        price = data[0][1]
        desc = data[0][2]
        bot.send_message(message.chat.id, f'Название товара: {name}\nЦена: {price}\nОписание: {desc}')
        bot.send_message(message.chat.id, 'Оформить заказ?', reply_markup=markup)
        bot.register_next_step_handler(message, confirm_offer)
    except:
        bot.send_message(message.chat.id, 'Такого товара не существует')
        bot.register_next_step_handler(message, return_db_data)


def confirm_offer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cancel_btn = types.KeyboardButton('Отмена')
    markup.add(cancel_btn)
    if message.text == 'Заказать':
        bot.send_message(message.chat.id, 'Введите адрес доставки (вводите правильно и без ошибок)',
                         reply_markup=markup)
        bot.register_next_step_handler(message, get_address)
    if message.text == 'Отмена':
        bot.message_handler(main_func(message))
    else:
        bot.register_next_step_handler(message, confirm_offer)


def get_address(message):
    if message.text == 'Отмена':
        bot.message_handler(main_func(message))
    address = message.text
    user_id = message.from_user.id
    offer_id = requests.post(f'http://127.0.0.1:8000/put_address_in_db?address={address}&prod_id={prod_id}&user_id={user_id}').json()
    offer_id = offer_id[0]
    bot.send_message(message.chat.id, f'Ваш заказ успешно зарегистрирован. ID товара: {prod_id}, '
                                      f'адрес доставки: {address}, номер заказа: {offer_id}')
    bot.message_handler(answer_on_offer(message))


bot.polling()
