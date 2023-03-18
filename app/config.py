class Config(object):
    DEBUG = True

    # DB URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # for develop model
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://dev:dev@db/dev'

class DevConfig(Config):
    """Development configuration."""
    ENV = 'dev'

class ProdConfig(Config):
    """Production configuration."""
    ENV = 'prod'
    DEBUG = False
    #SQLALCHEMY_DATABASE_URI = 'mysql://user:pass@prod_server:port/prod_db'
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar