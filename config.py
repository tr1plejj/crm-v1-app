# import psycopg2
# from config import user, host, password, db_name
host = 'localhost'
user = 'postgres'
password = 'Zxc1259663oliver'
db_name = 'prod_data'

# @bot.message_handler(commands=['s'])
# def message_in_channel(message):
#     try:
#         connection = psycopg2.connect(
#             host=host,
#             user=user,
#             password=password,
#             database=db_name
#         )
#         with connection.cursor() as cursor:
#             cursor.execute(f"insert into product values ('{name}', '{desc}', '{price}')")
#         connection.commit()
#     except Exception as _ex:
#         print('[INFO]', _ex)
#
#     finally:
#         if psycopg2.connect(
#                 host=host,
#                 user=user,
#                 password=password,
#                 database=db_name
#         ):
#             psycopg2.connect(
#                 host=host,
#                 user=user,
#                 password=password,
#                 database=db_name
#             ).close()

