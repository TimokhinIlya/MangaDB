from connect_db import *

# Установление соединения с базой данных
with create_connection() as conn:

    def new_manga_ins(name: str, cr_chap: int) -> None:
        # Проверка, установлено ли соединение с базой данных
        if conn:
            # Создание курсора для выполнения операций в базе данных
            cur = conn.cursor()
            try:
                # Формирование и выполнение операции INSERT для вставки новых данных в таблицу "manga"
                cur.execute(f'''
                    INSERT INTO dbo.manga (manga_name, current_chapter) VALUES (%s, %s)
                ''', (name, cr_chap))
                # Подтверждение изменений в базе данных
                conn.commit()
            except psycopg2.Error as e:
                # Вывод ошибки, если операция INSERT не выполнена успешно
                print(f"Error: {e}")
            finally:
                # Закрытие курсора после выполнения операции
                cur.close()

    def manga_chap_upd(name: str, cr_chap: int) -> None:
        if conn:
            cur = conn.cursor()
            try:
                # Обновление значения current_chapter для указанного manga_name в таблице "manga"
                cur.execute(f'''
                    UPDATE dbo.manga
                    SET current_chapter = %s
                    WHERE manga_name = %s
                ''', (cr_chap, name))
                conn.commit()
            except psycopg2.Error as e:
                # Вывод ошибки, если операция UPDATE не выполнена успешно
                print(f"Error: {e}")
            finally:
                cur.close()

    def manga_upd(url: str, l_chap: int, date: str, name: str) -> None:
        if conn:
            cur = conn.cursor()
            try:
                # Обновление значений manga_url, last_chapter и last_chapter_date для указанного manga_name в таблице "manga"
                cur.execute(f'''
                    UPDATE dbo.manga
                    SET manga_url = %s, last_chapter = %s, last_chapter_date = %s
                    WHERE manga_name = %s
                ''', (url, l_chap, date, name))
                conn.commit()
            except psycopg2.Error as e:
                print(f"Error: {e}")
            finally:
                cur.close()

    def manga_desc_upd(desc:str, name:str)-> None:
        if conn:
            cur = conn.cursor()
            try:
                # Обновление значения manga_desc для указанного manga_name в таблице "manga"
                cur.execute(f'''
                    UPDATE dbo.manga
                    SET manga_desc = %s
                    WHERE manga_name = %s
                ''', (desc, name))
                conn.commit()
            except psycopg2.Error as e:
                print(f"Error: {e}")
            finally:
                cur.close()

    def manga_query()-> list:
        if conn:
            cur = conn.cursor()
            try:
                # Выполнение операции SELECT для получения данных из таблицы "manga"
                cur.execute('''
                    SELECT manga_name, manga_url, current_chapter, last_chapter, last_chapter_date, manga_desc
                    FROM dbo.manga
                ''')
                rows = cur.fetchall()  # Получение всех данных
                conn.commit()

                # Создание списка словарей для хранения данных
                data = []
                for row in rows:
                    # Добавление словаря в список для каждой строки данных
                    data.append({
                        'manga_name': row[0],
                        'manga_url': row[1],
                        'current_chapter': row[2],
                        'last_chapter': row[3],
                        'last_chapter_date': str(row[4]),
                        'manga_desc': row[5]
                    })
                return data

            except psycopg2.Error as e:
                # Вывод ошибки, если операция SELECT не выполнена успешно
                print(f"Error: {e}")
            finally:
                cur.close()

    def manga_del(name:str)-> None:
        if conn:
            cur = conn.cursor()
            try:
                # Выполнение операции DELETE для удаления записи с указанным manga_name из таблицы "manga"
                cur.execute(f'''
                    DELETE FROM dbo.manga
                    WHERE manga_name = %s
                ''', (name, ))
                conn.commit()
            except psycopg2.Error as e:
                # Вывод ошибки, если операция DELETE не выполнена успешно
                print(f"Error: {e}")
            finally:
                cur.close()

    def get_manga_url(name:str)-> str:
        if conn:
            cur = conn.cursor()
            try:
                # Выполнение операции SELECT для получения значения manga_url по указанному manga_name из таблицы "manga"
                cur.execute(f'''
                    SELECT manga_url FROM dbo.manga
                    WHERE manga_name = %s
                ''', (name,))
                # Получение данных из базы данных
                url = cur.fetchall()
                conn.commit()
                # Возвращение значения URL
                return url[0][0]
            except psycopg2.Error as e:
                print(f"Error: {e}")
            finally:
                cur.close()