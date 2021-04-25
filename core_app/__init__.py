import os

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
