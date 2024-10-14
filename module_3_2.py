def send_mail(message, recipient,*, sender = "university.help@gmail.com"):
    if ('@' in recipient and '@' in sender) and (".com" or '.ru' or '.net') in recipient and (".com" or '.ru' or '.net') in sender:
        print(message)
    else:
        print('Невозможно отправить письмо с адреса <sender> на адрес <recipient>')
send_mail('проверка связи', "univer.help@gmail.com")


def send_mail(message, recipient,*, sender = "university.help@gmail.com"):
    if recipient == sender:
       print('Невозможно отправить письмо самому себе')
    else:
        print(message)
send_mail('письмо самому себе',"university.help@gmail.com")


def send_mail(message, recipient,*, sender = "university.help@gmail.com"):
    if sender == "university.help@gmail.com":
        print(message)
send_mail('Письмо успешно отправлено с адреса <sender> на адрес <recipient>',"univer.help@gmail.com")


def send_mail(message,recipient,*, sender = "university.help@gmail.com"):
    if  sender != "university.help@gmail.com":
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса university.info@gmail.com на адрес univer.help@gmail.com')
    else:
        print(message)
send_mail('Письмо успешно отправлено с адреса <sender> на адрес <recipient>',"univer.help@gmail.com", sender = "university.info@gmail.com")