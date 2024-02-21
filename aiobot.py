from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.enums import ParseMode
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import CommandStart, Command
import asyncio
import requests
from dotenv import load_dotenv
import os
import logging
import sys

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher()


class Offer(StatesGroup):
    id = State()
    address = State()
    is_confirmed = State()


@dp.message(CommandStart())
async def start(message: Message):
    make_offer = types.KeyboardButton(text='Сделать заказ')
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, keyboard=[[make_offer]])
    await message.answer('Для начала работы нажмите кнопку "Сделать заказ".', reply_markup=markup)


@dp.message(F.text == 'Сделать заказ')
async def get_offer(message: Message, state: FSMContext):
    await message.answer('Введите id желаемого товара')
    await state.set_state(Offer.id)


@dp.message(Offer.id)
async def hello(message: Message, state: FSMContext):
    global prod_id
    try:
        prod_id = message.text
        await state.update_data(id=prod_id)
        confirm = types.KeyboardButton(text='Заказать')
        cancel = types.KeyboardButton(text='Отмена')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[confirm, cancel]], one_time_keyboard=True)
        data = requests.get(f'http://127.0.0.1:8000/take_from_db/{prod_id}').json()
        name = data['name']
        price = data['price']
        desc = data['description']
        await message.answer(f'Название товара: {name}\nЦена: {price}\nОписание: {desc}\n\nОформить заказ?',
                               reply_markup=markup)
        await state.set_state(Offer.is_confirmed)
    except:
        await message.answer('Такого товара не существует. Введите id еще раз')
        await state.set_state(Offer.id)


@dp.message(Offer.is_confirmed)
async def confirm_offer(message: Message, state: FSMContext):
    if message.text == 'Отмена':
        await message.answer('Хорошо. Введите id другого товара')
        await state.set_state(Offer.id)
    elif message.text == 'Заказать':
        await state.update_data(is_confirmed=True)
        cancel = types.KeyboardButton(text='Отмена')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=[[cancel]])
        await bot.send_message(message.from_user.id, 'Введите адрес доставки\n!Вы можете нажать кнопку "Отмена" для выбора другого товара!',
                                reply_markup=markup)
        await state.set_state(Offer.address)
    else:
        await message.answer('Для продолжения нажмите либо "Заказать" либо "Отмена"')
        await state.set_state(Offer.is_confirmed)


@dp.message(Offer.address)
async def get_address(message: Message, state: FSMContext):
    if message.text == 'Отмена':
        await message.answer('Хорошо. Введите id другого товара')
        await state.set_state(Offer.id)
    else:
        make_offer = types.KeyboardButton(text='Сделать заказ')
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, keyboard=[[make_offer]])
        address = message.text
        await state.update_data(address=address)
        user_id = message.from_user.id
        offer_id = requests.post(f'http://127.0.0.1:8000/put_address_in_db?address={address}&prod_id={prod_id}&user_id={user_id}').text
        await message.answer(f'Ваш заказ успешно зарегистрирован. ID товара: {prod_id}, '
                                          f'адрес доставки: {address}, номер заказа: {offer_id}.', reply_markup=markup)
        all_data = await state.get_data()
        print(all_data.get('id'), all_data.get('is_confirmed'), all_data.get('address'))


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
