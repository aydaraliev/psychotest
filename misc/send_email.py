import smtplib
import traceback
from email.mime.text import MIMEText
from email.header    import Header

def send_email(user, pwd, recipient, subject, results):

    prepared_text = ""

    for characteristic in results:
        prepared_text = prepared_text + characteristic['title'] + '\n'
        prepared_text = prepared_text + characteristic['subtitle'] + '\n'
        prepared_text = prepared_text + characteristic['text'] + '\n'

    prepared_text = prepared_text.replace("extraversion", "Экстраверсия").replace("neuroticism", "Нейротизм").\
        replace("openness", "Открытость").replace("consciousness", "Сознательность").replace("friendly", "Доброжелательность")

    msg = MIMEText(prepared_text, 'plain', _charset="UTF-8")
    msg['Subject'] = Header(subject, "utf-8")
    msg['From'] = user
    msg['To'] = recipient[0]


    # FROM = user
    # TO = recipient if isinstance(recipient, list) else [recipient]
    # SUBJECT = subject
    # TEXT = prepared_text
    #
    # # Prepare actual message
    # message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    # """ % (FROM, ", ".join(TO), SUBJECT, TEXT)


    try:
        server = smtplib.SMTP("smtp.yandex.ru", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(user, recipient, msg.as_string())
        server.close()
        print('successfully sent the mail')
    except:
        traceback.print_exc()