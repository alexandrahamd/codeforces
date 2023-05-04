import psycopg2
from psycopg2 import Error


def get_db(rating):
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      # пароль, который указали при установке PostgreSQL
                                      password="12345",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="codeforces")

        cursor = connection.cursor()

        # cursor.execute("""select * from table_name where rating >= (%s) and tags = (%s) """, (str(rating), tag, ))
        cursor.execute("""select * from table_name where rating >= (%s)""", (str(rating), ))

        # cursor.execute(postgreSQL_select_Query)
        print("Выбор строк из таблицы mobile с помощью cursor.fetchall")
        mobile_records = cursor.fetchall()

        result = []
        i = 0
        while i < 10:
            for row in mobile_records:
                result.append(f'Номер: {row[0]}, Название: {row[1]}, Темы: {row[2]}')
                i += 1
            return result

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")

