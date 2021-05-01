import os
import smtplib
from email.message import EmailMessage

from celery import Celery


def make_celery():
    celery = Celery(
        __name__,
        # backend=os.environ['CELERY_RESULT_BACKEND'],
        broker=os.environ['CELERY_BROKER_URL']
    )
    return celery


celery = make_celery()


@celery.task
def send_email(address, text):
    sender = os.environ['SMTP_SENDER']
    pswd = os.environ['SMTP_PASSWORD']

    msg = EmailMessage()
    msg.set_content(text)
    msg['Subject'] = f'Message from {address}'
    msg['From'] = sender
    msg['To'] = 'self@sergeypavlov.dev'

    s = smtplib.SMTP_SSL('smtp.yandex.com', 465)
    s.login(sender, pswd)
    s.send_message(msg)
    s.quit()
