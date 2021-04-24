import os


class Config():
    SECRET_KEY = os.environ['SECRET_KEY']

    # Celery message queue
    CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']
    CELERY_RESULT_BACKEND = os.environ['CELERY_RESULT_BACKEND']


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    TEMPLATES_AUTO_RELOAD = True


class TestingConfig(Config):
    TEMPLATES_AUTO_RELOAD = True
    TESTING = True
    WTF_CSRF_ENABLED = False
