from flask import render_template,request,redirect,url_for,abort
from app import app



# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Kiru Flask Blog App"
    return render_template('index.html',title=title)

# About route and view function
@app.route('/about')
def about():
    return render_template("about.html",title = "About")