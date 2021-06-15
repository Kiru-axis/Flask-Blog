from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
# generating_password_hash - This function takes in a password and generates a password hash.
# check_password_hash - This function takes in a hash password and a password entered by a user and checks if the password matches to return a True or False response.
from flask_login import UserMixin
# implements is_authenticated(),is_active(),is_anonymous(),get_id() functions
from . import login_manager


# Flask-login has a decorator @login_manage.user_loader that modifies the load_userfunction by passing in a user_id to the function that queries the database and gets a User with that ID.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
# user
class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), unique = True, index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String)    
    password_hash = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref = 'users', lazy = 'dynamic')
    comments = db.relationship('Comment', backref = 'users', lazy = 'dynamic')

    def __repr__(self):
        return f'User {self.username}'

# @property decorator creates a write only class property password. 
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


# pitch
class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    pitch_content = db.Column(db.String)
    category = db.Column(db.String(255))
    author = db.Column(db.String(255))
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)        
    published_at = db.Column(db.DateTime, default = datetime.utcnow)    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref = 'pitches', lazy = 'dynamic')

# comment
class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)    
    body = db.Column(db.String)          
    published_at = db.Column(db.DateTime, default = datetime.utcnow)    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    
    # saving comments to the database
    def save_comment(self):
        db.session.add(self)
        db.session.commit()