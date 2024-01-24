import psycopg2
# from config import user, host, password, db_name
host = 'localhost'
user = 'postgres'
password = 'Zxc1259663oliver'
db_name = 'products_data'
def add_in_db(name, price, description):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        with connection.cursor() as cursor:
            cursor.execute(f"insert into prod_data(name, price, description) values ('{name}', '{price}', '{description}')")
            cursor.execute("select id from prod_data order by id desc limit 1")
            last_id = cursor.fetchone()
        connection.commit()
        return last_id
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
