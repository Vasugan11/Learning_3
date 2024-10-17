def send_mail(message, recipient,*, sender = "university.help@gmail.com"):
    if ('@' not in recipient or '@' not in sender) or not recipient.endswith((".com", '.ru', '.net')) or not sender.endswith((".com", '.ru', '.net')):
        print(f'Невозможно отправить письмо с адреса {sender} на адреc {recipient}')

    elif recipient == sender:
       print('Нельзя отправить письмо самому себе')

    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')

    elif sender != "university.help@gmail.com":
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

    else:
        print('Письмо успешно отправлено')


send_mail('проверка ошибок в адресах',"univer.helpgmail.com")             # нет @
send_mail('письмо самому себе', 'university.help@gmail.com')
send_mail('правильный адрес <sender>', 'univer.help@gmail.com')
send_mail('Проверка отправителя',"univer.help@gmail.com", sender = "university.info@gmail.com")