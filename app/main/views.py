from flask import render_template,request,redirect,url_for,abort
from .import main
from flask_login import login_required
# login required checks if the user is logged in
from app.models import User
from .forms import UpdateProfile,PitchForm,CommentsForm
from ..import db



# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Flask Blog"
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


# profile view Function
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)



# fetching grom the databse
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


# fetching the photos from the db
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))