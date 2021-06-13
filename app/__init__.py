from flask import Flask
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()

# Initializing application
app = Flask(__name__)

# Initializing Flask bootstrap Extension
bootstrap = Bootstrap(app)



from app import views