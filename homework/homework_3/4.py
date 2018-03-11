# Обращение в письмах начинаются с фразы “Dear Mr./Mrs./Miss/Ms. ...“.
# Необходимо определить и вывести пол человека, которому данное письмо адресовано.
# Приглашение письма запрашивается у пользователя.
message = input()
if 'Dear Mr.' in message:
    print('Male')
elif 'Dear Miss.' in message or 'Dear Ms.' in message or 'Dear Mrs.' in message:
    print('Female')
