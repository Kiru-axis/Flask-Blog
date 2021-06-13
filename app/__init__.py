from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()

# creating an instance of Sqlalchemy
db = SQLAlchemy()

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

    return app