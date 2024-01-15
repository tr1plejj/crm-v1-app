import telebot
import psycopg2
from config import user, host, password, db_name

TOKEN = '6095405341:AAGVEIaNq0i6qdISCC2VtM3r3aExJN0jwQI'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['s'])
def message_in_channel(message):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        with connection.cursor() as cursor:
            cursor.execute(f"insert into product values ('{name}', '{desc}', '{price}')")
        connection.commit()
    except Exception as _ex:
        print('[INFO]', _ex)

    finally:
        if psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
        ):
            psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            ).close()

bot.polling()
