from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField, validators
from wtforms.widgets import TextArea
from wtforms.fields.html5 import EmailField

class ContactForm(FlaskForm):
    name = StringField('Name: ')
    email = EmailField('Email address:', [validators.DataRequired(), validators.Email()])
    message = StringField('Message: ',widget=TextArea())
    submit = SubmitField('Submit')
