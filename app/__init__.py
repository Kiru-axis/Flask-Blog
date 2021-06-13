from flask import Flask
from flask_bootstrap import Bootstrap
from .config import DevConfig

bootstrap = Bootstrap()

# Initializing application
app = Flask(__name__)

# Initializing Flask bootstrap Extension
bootstrap = Bootstrap(app)

# setting up configs
app.config.from_object(DevConfig)


from app import views