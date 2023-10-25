import psycopg2

def create_connection():
    try:
        # Попытка установить соединение с базой данных PostgreSQL
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Cthuttdbx7",
            host="localhost",
            port="5432"
        )
        # Возвращаем соединение, если подключение установлено успешно
        return conn
    except psycopg2.Error as e:
        # В случае ошибки выводим сообщение об ошибке
        print(f"Ошибка: Подключение к PostgreSQL не удалось. {e}")
        return None