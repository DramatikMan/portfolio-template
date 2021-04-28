from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class MessageForm(FlaskForm):
    address = StringField('Your email', [DataRequired(), Email()])
    text = TextAreaField('Your message', [DataRequired(), Length(min=10)])
