from flask import render_template,request,redirect,url_for,abort
from .import main
from flask_login import login_required
# login required checks if the user is logged in


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Kiru Flask Blog App"
    return render_template('index.html',title=title)

# login routes
@main.route('/login')
@login_required
def login():
    return render_template('login.html')
# About route and view function
@main.route('/about')
def about():
    return render_template("about.html",title = "About")