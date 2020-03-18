import os
import smtplib
import imghdr
from email.message import EmailMessage

SMTP_ADDRESS = 'smtp.gmail.com'
SMTP_PORT = 465

EMAIL_ADDRESS = os.environ['EMAIL_ADDRESS']
EMAIL_PASS = os.environ['EMAIL_PASS']


def send_email(msg_to, subject, msg_body, image=None):
    msg = EmailMessage()
    msg['To'] = msg_to
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg.set_content(msg_body)

    if image is not None:
        with open(image, 'rb') as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name

        msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

    try:
        with smtplib.SMTP_SSL(SMTP_ADDRESS, SMTP_PORT) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
            smtp.send_message(msg)
    except:
        print('Failed to send message')
