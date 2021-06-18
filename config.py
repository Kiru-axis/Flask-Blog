import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY') 
    #specifies the destination to where we want to store our Images
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS= True


    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    # mail_use_tls:true Enables a transport layer security to secure the emails when sending emails
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://axs:code@localhost/blog_test'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","")
    
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI =SQLALCHEMY_DATABASE_URI.replace("postgres://","postgresql://",1)

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
     # this is the location of the database with authentication.

    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://axs:code@localhost/blog'
    
    DEBUG = True

#These dictionary help us access different configuration option classes.
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}