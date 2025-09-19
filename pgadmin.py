# import psycopg2
# conn = psycopg2.connect(
#     dbname="nt",
#     user="postgres",
#     password="123",
#     host="localhost", #127.0.0.1
#     port="5432"
# )
# cur = conn.cursor()
# sql1 = '''
# select * from categories
# '''
#
# s2 = '''
#
# '''
#
# # Malumot qo‘shish
#
# cur.execute(sql1)
# s = cur.fetchall()
# print(s)
# for item in s:
#     print(item[0],item[1])
#
# conn.commit()
# cur.close()
# conn.close()

import psycopg2

# 🔑 PostgreSQL ma'lumotlari
host="localhost"
database="mydb"
user="postgres"
password="12345"
DB_PORT = "5432"

def get_connection():
    return psycopg2.connect(
        dbname=database,
        user=user,
        password=password,
        host=host,
        port=DB_PORT
    )

def init_db():
    """Agar jadval bo‘lmasa yaratadi."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            phone VARCHAR(20) UNIQUE NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()