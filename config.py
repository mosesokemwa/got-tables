"""Flask config class."""
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """Set Flask configuration vars."""
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

    """Base config vars."""
    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS=os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    SECRET_KEY=os.environ.get('SECRET_KEY')
    API_ENDPOINT=os.environ.get('API_ENDPOINT')


class ProductionConfig(Config):
    DEBUG = False



class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True