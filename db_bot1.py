import sqlite3 as sq
from datetime import datetime



def save_to_database(data):
    try:
        with sq.connect('base.db') as conn:
            cur = conn.cursor()

            cur.execute("""
                INSERT INTO user(first_name, last_name, age)
                VALUES (?, ?, ?)""",
                (data['first_name'], data['last_name'], data['age']))
            conn.commit()
    except sq.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

