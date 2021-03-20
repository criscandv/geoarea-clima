import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    DEBUG = False
    TESTING = False
    SECRET_KEY = '}+?0?!O??zo?V;?7??I@ ?O?@K,'
    SQLALCHEMY_DATABASE_URI = 'postgresql://example:thisisthepass@192.168.1.73/db_clima'
    CLIMATE_API_KEY = 'XxTzqqz4qa4BXaq'


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
