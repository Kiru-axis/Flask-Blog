from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError
# registration form

class RegistrationForm(FlaskForm):
    email = StringField('Email Address', validators=[Required(), Email()])
    username = StringField('Enter your username', validators = [Required()])
    password = PasswordField('Password', validators = [Required(), EqualTo('password_confirm', message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Password', validators =[Required()])
    submit = SubmitField('Sign Up')
# custom validators
    # validate username
    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')


    # validate email
    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')


# Login forms
class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
   # for confirming whether the user wants to be logged out after the session 
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
