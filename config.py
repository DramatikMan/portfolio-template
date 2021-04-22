import os


class Config():
    SECRET_KEY = os.environ['SECRET_KEY']


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    TEMPLATES_AUTO_RELOAD = True


class TestingConfig(Config):
    TEMPLATES_AUTO_RELOAD = True
    TESTING = True
    WTF_CSRF_ENABLED = False
