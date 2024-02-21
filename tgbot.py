import asyncio
import requests
from telebot.async_telebot import AsyncTeleBot
from telebot.async_telebot import types
import logging
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = AsyncTeleBot(TOKEN)


@bot.message_handler(commands=['start'])
async def main_func(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    id_button = types.KeyboardButton('Сделать заказ')
    markup.add(id_button)
    await bot.send_message(message.from_user.id, text='Нажмите кнопку "Сделать заказ" для продолжения', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Сделать заказ')
async def answer_on_offer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    no = types.KeyboardButton('Отмена')
    markup.add(no)
    await bot.send_message(message.from_user.id, 'Введите id товара', reply_markup=markup)
    bot.register_message_handler(return_db_data)


async def return_db_data(message):
    global prod_id
    if message.text == 'Отмена':
        bot.register_message_handler(await main_func(message))
    else:
        try:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            confirm = types.KeyboardButton('Заказать')
            cancel = types.KeyboardButton('Отмена')
            markup.row(confirm, cancel)
            prod_id = message.text
            data = requests.get(f'http://127.0.0.1:8000/take_from_db/{prod_id}').json()
            print(data)
            name = data['name']
            price = data['price']
            desc = data['description']
            await bot.send_message(message.from_user.id, f'Название товара: {name}\nЦена: {price}\nОписание: {desc}\n\nОформить заказ?',
                                       reply_markup=markup)
            bot.register_message_handler(confirm_offer)
        except Exception as e:
            print(e)
            await bot.send_message(message.from_user.id, 'Такого товара не существует')
            bot.register_message_handler(return_db_data)


async def confirm_offer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cancel_btn = types.KeyboardButton('Отмена')
    markup.add(cancel_btn)
    if message.text == 'Заказать':
        await bot.send_message(message.from_user.id, 'Введите адрес доставки (вводите правильно и без ошибок)',
                         reply_markup=markup)
        bot.register_message_handler(get_address)
    if message.text == 'Отмена':
        bot.register_message_handler(await main_func(message))
    else:
        bot.register_message_handler(confirm_offer)


async def get_address(message):
    if message.text == 'Отмена':
        bot.register_message_handler(main_func)
    address = message.text
    user_id = message.from_user.id
    offer_id = requests.post(f'http://127.0.0.1:8000/put_address_in_db?address={address}&prod_id={prod_id}&user_id={user_id}').text
    await bot.send_message(message.chat.id, f'Ваш заказ успешно зарегистрирован. ID товара: {prod_id}, '
                                      f'адрес доставки: {address}, номер заказа: {offer_id}')
    bot.register_message_handler(answer_on_offer)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.polling()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
# убрать постоянное создание кнопки отмена