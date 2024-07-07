calls = 0


def send_email(message, recipient, sender="university.help@gmail.com"):
  """
  Отправляет электронное письмо с проверкой на корректность адресов и отправителя.

  Args:
      message (str): Текст сообщения.
      recipient (str): Адрес получателя.
      sender (str, optional): Адрес отправителя.
                                По умолчанию: "university.help@gmail.com".

  Returns:
      None: Функция выводит результат в консоль.
  """

  if not ("@" in recipient and recipient.endswith((".com", ".ru", ".net")) and \
          "@" in sender and sender.endswith((".com", ".ru", ".net"))):
    print(f"Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>")
  elif sender == recipient:
    print("Нельзя отправить письмо самому себе!")
  elif sender == "university.help@gmail.com":
    print(f"Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>.")
  else:
    print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>.")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение просто так!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
