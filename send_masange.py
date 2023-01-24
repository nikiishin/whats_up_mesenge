#pip install pywhatkit

import pywhatkit


def send_massage_inst():
    mobile = input('Введите номер:')
    massege = input('Введите сообщение:')
    pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=massege)

def send_massage():
    mobile = input('Введите номер:')
    massege = input('Введите сообщение:')
    hour = int(input('Введите часы:'))
    minutes = int(input('Введите минуты:'))
    pywhatkit.sendwhatmsg(phone_no=mobile, message=massege, time_hour=hour, time_min=minutes)




def main():
    # send_massage_inst()

    send_massage()

if __name__ == '__main__':
    main()

