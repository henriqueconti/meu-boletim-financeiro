from app.utils.database import get_conn_db_users_tickers

DB_CONN = get_conn_db_users_tickers()


def get_users():
    global DB_CONN
    if DB_CONN is None:
        DB_CONN = get_conn_db_users_tickers()

    cursor = DB_CONN.cursor()
    cursor.execute("SELECT * FROM db_users_tickers LIMIT 10 OFFSET 0;")
    cursor.fetchall()
