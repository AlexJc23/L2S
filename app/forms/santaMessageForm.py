from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError


def phone_digits(form, field):
    phone_number = field.data
    if not phone_number.isdigit() or len(phone_number) != 10:
        raise ValidationError('Provide a valid 10-digit phone number.')


def contact_info_required(form, field):
    if not form.phone_number.data and not form.email.data:
        raise ValidationError('Please provide at least a phone number or email.')


class SantaMessageForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[phone_digits, contact_info_required])
    email = StringField('Email', validators=[Email(), contact_info_required])
    message = StringField('Message', validators=[DataRequired()])
