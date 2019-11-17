from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Required])
    submit = SubmitField('Send')

