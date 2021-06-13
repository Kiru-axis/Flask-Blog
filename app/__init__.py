from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
# UploadSet: defines the types of files to upload
from flask_mail import Mail


bootstrap = Bootstrap()

# creating an instance of Sqlalchemy
db = SQLAlchemy()

# login extension for management of user authentication
login_manager = LoginManager()
login_manager.session_protection = 'strong' #provides security levels
login_manager.login_view = 'auth.login'

# Telling uploadSet the type to be uploaded is an image
photos = UploadSet('photos',IMAGES)

# crearing instance of the mail
mail = Mail()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

# Initializing flask extensions
    # initialising bootstrap
    bootstrap.init_app(app)
    # initialising sqlalchemy
    db.init_app(app)

    # registering auth blueprint
    # url_prefix: adds a prefix to all routes registerd with that blueprint
    from .auth import auth as auth_blueprint
    app.register_auth(auth_blueprint,url_prefix='/authenticate')

    # initalising flasks LoginManger
    login_manager.init_app(app)

    # configuring UploadSet
    configure_uploads(app,photos)

    # initialsing mail
    mail.init_app(app)


    return app