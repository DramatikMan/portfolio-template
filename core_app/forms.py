from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class MessageForm(FlaskForm):
    email = StringField('Email', [DataRequired(), Email()])
    message = TextAreaField('Message', [DataRequired()])
