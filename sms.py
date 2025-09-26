# sms yuborish, sms tarixi, sms ochirish,chiqqish

from contact import *
sms_data={}
class SMS:
    def __init__(self,id,phone,sms):
        self.id=id
        self.phone=phone
        self.sms=sms
def send_sms():
    phone="+998"+input("Telefon raqamni kiriting: ")
    send_smsSQL(phone)



def show_history():
    show_historySQL()

# def delete_sms():
#     phone_number="+998"+input("Telefon raqam kiriting: ")
#     exist = False
#     for contact in data_contact:
#         if contact.phone == phone_number:
#             exist = True
#             break
#     if exist:
#         print("SMS tarixi\n")
#         for key, value in sms_data.items():
#             if key==phone_number:
#                 print(f"Telefon raqam: {key}")
#                 for i in value:
#                     print(f"{i.id}. {i.sms}")
#                 break
#         delete_id=input("SMS id sini kiriting: ")
#         sms_list=sms_data[phone_number]
#
#         for sms in sms_list:
#             if sms.id==delete_id:
#                 sms_list.remove(sms)
#                 print("SMS o'chirildi")
#                 return
#         print("Bunday ID yo'q")
#
#     else:
#         print("Bunday telefon raqam mavjud emas!")
