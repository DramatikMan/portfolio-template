import os
import smtplib
from email.message import EmailMessage

from celery import Celery


def make_celery():
    celery = Celery(
        __name__,
        backend=os.environ['CELERY_RESULT_BACKEND'],
        broker=os.environ['CELERY_BROKER_URL']
    )
    return celery


celery = make_celery()


@celery.task
def log(msg):
    return msg


@celery.task
def send_email(email, text):
    msg = EmailMessage()
    msg.set_content(text)
    msg['Subject'] = 'Contact form message'
    msg['From'] = email
    msg['To'] = 'self@sergeypavlov.dev'

    s = smtplib.SMTP('127.0.0.1', 8025)
    s.send_message(msg)
    s.quit()
