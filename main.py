#6095405341:AAGVEIaNq0i6qdISCC2VtM3r3aExJN0jwQI
#https://api.telegram.org/bot6095405341:AAGVEIaNq0i6qdISCC2VtM3r3aExJN0jwQI/getChat?chat_id=@fastsellandresell

import telebot

TOKEN = '6095405341:AAGVEIaNq0i6qdISCC2VtM3r3aExJN0jwQI'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['send'])
def message_in_channel(message):
    bot.send_message(-1002112682526, 'im here')

bot.infinity_polling()