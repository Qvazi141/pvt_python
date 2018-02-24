# Обращение в письмах начинаются с фразы “Dear Mr./Mrs./Miss/Ms. ...“.
# Необходимо определить и вывести пол человека, которому данное письмо адресовано.
# Приглашение письма запрашивается у пользователя.
message = input()
if 'Mr.' in message or 'Mrs.' in message:
    print('Male')
elif 'Miss.' in message or 'Ms.' in message:
    print('Female')
