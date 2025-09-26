from sms import *
from contact import *

while True:
    print("1 - SMS\n2 - Kontakt\n3 - Chiqish")
    operation_key = int(input("Kiriting: "))
    clear_console()
    if operation_key ==1:
        print("1 - sms tarixi\n2 - sms yuborish\n3 - sms o'chirish\n4 - Chiqish")
        key=int(input("Kiriting: "))
        if key==1:
            show_history()
        elif key==2:
            send_sms()
        elif key ==3:
            delete_sms()
        else:
            clear_console()
            break
    elif operation_key==2:
        while True:
            print(
                "1 - Ma'lumotlarni ko'rish\n2 - Ma'lumot qo'shish\n3 - Ma'lumot o'chirish\n4 - Ma'lumot o'zgartirish\n5 - Chiqish")
            key = int(input("Kiriting: "))
            # Ma'lumotlarni ko'rish
            if key == 1:
                clear_console()
                show_contacts()
            # Ma'lumot qo'shish
            elif key == 2:
                clear_console()
                add_contact()
            # Ma'lumot o'chirish
            elif key == 3:
                clear_console()
                delete_contact()
            # Ma'lumot o'zgartirish
            elif key == 4:
                clear_console()
                change_contact()
            # Chiqish
            else:
                clear_console()
                break
    else:
        print("Tamom")
        break
