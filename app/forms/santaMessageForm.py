from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError



class SantaMessageForm(FlaskForm):
    first_name = StringField('first_name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    message = StringField('message', validators=[DataRequired()])
