from connect_db import *

SCHEMA_NAME = "dbo"
TABLE_NAME = "manga"
NAME_FIELD = "manga_name"
URL_FIELD = "manga_url"
CUR_CHAPTER = "current_chapter"
LAST_CHAPTER = "last_chapter"
CHAPTER_DATE = "manga_chapter_date"

def manga_ins(name, cur):
    conn = create_connection()
    if conn:
        cur = conn.cursor()
        try:
            cur.execute(f'''
                INSERT INTO {TABLE_NAME} ({NAME_FIELD}, {CUR_CHAPTER}) VALUES (%s, %s)
            ''', (name, cur))
            conn.commit()
        except psycopg2.Error as e:
            print(f"Error: {e}")
        finally:
            cur.close()
            conn.close()

def manga_upd(name, new_age):
    conn = create_connection()
    if conn:
        cur = conn.cursor()
        try:
            cur.execute(f'''
                UPDATE {TABLE_NAME}
                SET {AGE_FIELD} = %s
                WHERE {NAME_FIELD} = %s
            ''', (new_age, name))
            conn.commit()
        except psycopg2.Error as e:
            print(f"Error: {e}")
        finally:
            cur.close()
            conn.close()