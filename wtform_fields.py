from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
  """ Registration form """ 

  username = StringField('username_label', validators=[InputRequired(message="Username Required"), Length(min=3, message="Username must be at least 3 characters")])
  password = PasswordField('password_label', validators=[InputRequired(message="Password Required"), Length(min=8, message="Username must be at least 8 characters")])
  confirm_pswd = PasswordField('confirm_pswd_label', validators=[InputRequired(message="Password Required"), EqualTo('password', message="Passwords Must Match")])
  submit_button = SubmitField('Create')