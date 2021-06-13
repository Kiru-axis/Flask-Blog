import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY') 
     # this is the location of the database with authentication.
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://axs:code@localhost/blog'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

#These dictionary help us access different configuration option classes.
config_options = {
'development':DevConfig,
'production':ProdConfig,
}