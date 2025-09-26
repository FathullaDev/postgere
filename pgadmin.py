# # import psycopg2
# # conn = psycopg2.connect(
# #     dbname="nt",
# #     user="postgres",
# #     password="123",
# #     host="localhost", #127.0.0.1
# #     port="5432"
# # )
# # cur = conn.cursor()
# # sql1 = '''
# # select * from categories
# # '''
# #
# # s2 = '''
# #
# # '''
# #
# # # Malumot qo‘shish
# #
# # cur.execute(sql1)
# # s = cur.fetchall()
# # print(s)
# # for item in s:
# #     print(item[0],item[1])
# #
# # conn.commit()
# # cur.close()
# # conn.close()
#
# import psycopg2
#
# # 🔑 PostgreSQL ma'lumotlari
# host="localhost"
# database="mydb"
# user="postgres"
# password="12345"
# DB_PORT = "5432"
#
# def get_connection():
#     return psycopg2.connect(
#         dbname=database,
#         user=user,
#         password=password,
#         host=host,
#         port=DB_PORT
#     )
#
# def init_db():
#     """Agar jadval bo‘lmasa yaratadi."""
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS contacts (
#             id SERIAL PRIMARY KEY,
#             name VARCHAR(100) NOT NULL,
#             email VARCHAR(100) UNIQUE NOT NULL,
#             phone VARCHAR(20) UNIQUE NOT NULL
#         );
#     """)
#     conn.commit()
#     cur.close()
#     conn.close()


import psycopg2

from contact import add_contact

# 'host=localhost user=postgres password=123 dbname=nt'
connection=psycopg2.connect(
    host='localhost',
    user='postgres',
    password='123',
    dbname='nt'
)
cursor=connection.cursor()

def add_contactSQL(name,phone,email):
    cursor.execute(f"INSERT INTO contact VALUES({name},{phone},{email})")
    connection.commit()
    cursor.close()
    connection.close()

def delete_contactSQL(delete_id):
    cursor.execute(f"DELETE FROM contact WHERE id = {delete_id}")
    connection.commit()
    cursor.close()
    connection.close()

def change_contactSQL(change_id,new_name,new_phone,new_email):
    cursor.execute(f"UPDATE contact SET name ={new_name}, phone={new_phone}, email={new_email} WHERE id={change_id}")
    connection.commit()
    cursor.close()
    connection.close()

def send_smsSQL(phone):
    cursor.execute(f"SELECT 1 FROM contact WHERE phone = {phone}")
    exists = cursor.fetchone()
    if exists:
        sms = input("SMS kiriting: ")
        cursor.execute(f"INSERT INTO sms VALUES({phone},{sms})")
        connection.commit()
        cursor.close()
        connection.close()
    else:
        print("Bunday telefon raqam mavjud emas!")

def show_historySQL():
    cursor.execute("SELECT EXISTS (SELECT 1 FROM sms)")
    has_data = cursor.fetchone()[0]

    if has_data:
        cursor.execute("SELECT * FROM sms")
        rows=cursor.fetchall()

        for row in rows:
            print(row)
    else:
        print("Jadval bo'sh!")
    cursor.close()
    connection.close()
