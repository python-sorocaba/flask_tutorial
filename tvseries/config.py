from decouple import config


class BaseConfig(object):
    SITE_NAME = 'Flask Tutorial'
    SECRET_KEY = config('SECRET_KEY')
    SERVER_NAME = config('SERVER_NAME')
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tvseries-test.sqlite3'
    TESTING = True


class ProductionConfig(BaseConfig):
    pass
