import telebot
import psycopg2

TOKEN = '6095405341:AAGVEIaNq0i6qdISCC2VtM3r3aExJN0jwQI'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['s'])
def message_in_channel(message):

    bot.send_message(-1002112682526, '')

bot.polling()
