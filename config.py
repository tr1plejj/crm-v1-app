# import psycopg2
host = 'localhost'
user = 'postgres'
password = 'Zxc1259663oliver'
db_name = 'prod_data'

# try:
#     connection = psycopg2.connect(
#         host=host,
#         user=user,
#         password=password,
#         database=db_name
#     )
#     with connection.cursor() as cursor:
#         cursor.execute(f"""INSERT INTO product (name, description, price) VALUES ({name}, {desc}, {price});""")
#     connection.commit()
# except Exception as _ex:
#     print('[INFO]', _ex)
#
# finally:
#     if psycopg2.connect(
#             host=host,
#             user=user,
#             password=password,
#             database=db_name
#     ):
#         psycopg2.connect(
#             host=host,
#             user=user,
#             password=password,
#             database=db_name
#         ).close()
