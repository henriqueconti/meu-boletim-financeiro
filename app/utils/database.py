import os
import psycopg2


def get_conn_db_users_tickers():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS')
        )
        return conn
    except psycopg2.OperationalError as e:
        print(f"Falha ao conectar ao PostgreSQL: {e}")
