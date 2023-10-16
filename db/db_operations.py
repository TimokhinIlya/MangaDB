from connect_db import *

SCHEMA_NAME = "dbo"
TABLE_NAME = "manga"
ID_FIELD = ""
NAME_FIELD = ""
AGE_FIELD = ""

def manga_ins(name, age):
    conn = create_connection()
    if conn:
        cur = conn.cursor()
        try:
            cur.execute(f'''
                INSERT INTO {TABLE_NAME} ({NAME_FIELD}, {AGE_FIELD}) VALUES (%s, %s)
            ''', (name, age))
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