import os
import re
import sys

from pgadmin import *

data_contact=[]
class Contact:
    def __init__(self,name,phone,email):
        self.name=name
        self.phone="+998" + phone
        self.email=email

def show_contacts():
    if not data_contact:
        print("Ma'lumot yo'q")
    else:
        for contact in data_contact:
            print(f"Name - {contact.name}  Phone - {contact.phone}  Email - {contact.email}")

def add_contact():
    while True:
        name = input("Name: ")
        if not check_name(name):
            print("Noto'gri kiritildi. Qaytadan urining!")
        else: break

    while True:
        phone = input("Phone: ")
        if not check_phone(phone):
            print("Noto'gri kiritildi. Qaytadan urining!")
        else:break

    while True:
        email=input("Email: ")
        if not check_email(email):
            print("Noto'gri kiritildi. Qaytadan urining!")
        else: break

    add_contactSQL(name,phone,email)
    # contact=Contact(name,phone,email)
    # data_contact.append(contact)
    print("Ma'lumot muvaffaqiyatli qo'shildi!")

def delete_contact():
    delete_id=input("ID ni kiriting: ")
    delete_contactSQL(delete_id)

def change_contact():
    new_name=None
    new_phone=None
    new_email=None
    change_id=input("ID ni kiriting: ")
    change_key = int(input("Nameni o'zgartirasizmi?\n1 - Ha\n2 - Yo'q\nKiriting:"))
    if change_key == 1:
        while True:
            new_name = input("Name: ")
            if not check_name(new_name):
                print("Noto'gri kiritildi. Qaytadan urining!")
            else:
                break

    change_key = int(input("Phoneni o'zgartirasizmi?\n1 - Ha\n2 - Yo'q\nKiriting:"))
    if change_key == 1:
        while True:
            new_phone = input("Phone: ")
            if not check_phone(new_phone):
                print("Noto'gri kiritildi. Qaytadan urining!")
            else:
                break

    change_key = int(input("Emailni o'zgartirasizmi?\n1 - Ha\n2 - Yo'q\nKiriting:"))
    if change_key == 1:
        while True:
            new_email = input("Email: ")
            if not check_email(new_email):
                print("Noto'gri kiritildi. Qaytadan urining!")
            else:
                break
    change_contactSQL(change_id,new_name,new_phone,new_email)

def check_name(name):
    r_name = r"^[A-Z][a-z]{2,15}$"
    return bool(re.match(r_name,name))

def check_phone(phone):
    r_name = r"^[0-9]{9}$"
    return bool(re.match(r_name,phone))

def check_email(email):
    r_name = r"[^@ \t\r\n\.]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
    return bool(re.match(r_name,email))

def clear_console():
    if sys.stdout.isatty():
        os.system('cls' if os.name=='nt' else 'clear')
    else:
        print("\n"*30)
