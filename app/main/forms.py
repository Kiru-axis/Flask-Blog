from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, RadioField
from wtforms.validators import Required

# users thoughts
class PitchForm(FlaskForm):
    title = StringField('Pitch Title', validators=[Required()])
    author = StringField('Author', validators=[Required()])
    pitch_content = TextAreaField('Write Pitch', validators=[Required()])  
    category = RadioField('Pick Category', choices=[('Pickup Lines', 'Pickup Lines'), ('Interview Pitch', 'Interview Pitch'), ('Product Pitch', 'Product Pitch'), ('Promotion Pitch', 'Promotion Pitch')], validators=[Required()])  
    submit = SubmitField('Submit')

# updating the users thoughts
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Say something about yourself...', validators = [Required()])
    submit = SubmitField('Submit')
# comments section
class CommentsForm(FlaskForm):
    body = TextAreaField('Write a comment...', validators=[Required()])
    submit = SubmitField('Submit')