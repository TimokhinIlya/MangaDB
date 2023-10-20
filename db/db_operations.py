from connect_db import *
import json

def new_manga_ins(name:str, cr_chap:int)-> None:
    conn = create_connection()
    if conn:
        cur = conn.cursor()
        try:
            cur.execute(f'''
                INSERT INTO dbo.manga (manga_name, current_chapter) VALUES (%s, %s)
            ''', (name, cr_chap))
            conn.commit()
        except psycopg2.Error as e:
            print(f"Error: {e}")
        finally:
            cur.close()
            conn.close()

def manga_chap_upd(name:str, cr_chap:int)-> None:
    conn = create_connection()
    if conn:
        cur = conn.cursor()
        try:
            cur.execute(f'''
                UPDATE dbo.manga
                SET current_chapter = %s
                WHERE manga_name = %s
            ''', (cr_chap, name))
            conn.commit()
        except psycopg2.Error as e:
            print(f"Error: {e}")
        finally:
            cur.close()
            conn.close()

def manga_upd(url:str, l_chap:int, date:str, name:str)-> None:
    conn = create_connection()
    if conn:
        cur = conn.cursor()
        try:
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
            conn.close()

def manga_desc_upd(desc:str, name:str)-> None:
    conn = create_connection()
    if conn:
        cur = conn.cursor()
        try:
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
            conn.close()

def manga_query()-> json:
    conn = create_connection()
    if conn:
        cur = conn.cursor()
        try:
            cur.execute('''
                SELECT manga_name, manga_url, current_chapter, last_chapter, last_chapter_date, manga_desc
                FROM dbo.manga
            ''')
            rows = cur.fetchall()  # Получение всех данных
            conn.commit()

            # Создание словаря
            data = []
            for row in rows:
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
            print(f"Error: {e}")
        finally:
            cur.close()
            conn.close()

def manga_del(name:str)-> None:
    conn = create_connection()
    if conn:
        cur = conn.cursor()
        try:
            cur.execute(f'''
                DELETE FROM dbo.manga
                WHERE manga_name = %s
            ''', (name, ))
            conn.commit()
        except psycopg2.Error as e:
            print(f"Error: {e}")
        finally:
            cur.close()
            conn.close()

def get_manga_url(name:str)-> str:
    conn = create_connection()
    if conn:
        cur = conn.cursor()
        try:
            cur.execute(f'''
                SELECT manga_url FROM dbo.manga
                WHERE manga_name = %s
            ''', (name, ))
            url = cur.fetchall()
            conn.commit()
            return url[0][0]
        except psycopg2.Error as e:
            print(f"Error: {e}")
        finally:
            cur.close()
            conn.close()