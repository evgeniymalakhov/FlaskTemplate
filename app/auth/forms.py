from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import InputRequired, Email, Length, Regexp, EqualTo
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        InputRequired(),
        Length(1, 64),
        Email()])
    password = PasswordField('Password', validators=[
        InputRequired()
    ])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[
        InputRequired(),
        Length(1, 64),
        Email()])
    username = StringField('Username', validators=[
        InputRequired(),
        Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Username must have only letters, numbers, dots or underscores')
    ])
    password = PasswordField('Password', validators=[
        InputRequired(),
        EqualTo('password2', message='Passwords must match.')
    ])
    password2 = PasswordField('Password', validators=[
        InputRequired()
    ])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already in use.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
