import psycopg2

def create_connection():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Cthuttdbx7",
            host="localhost",
            port="5432"
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error: Could not connect to PostgreSQL. {e}")
        return None