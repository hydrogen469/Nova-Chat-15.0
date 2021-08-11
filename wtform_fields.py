from flask_wtf import FlaskForm
from passlib.hash import pbkdf2_sha256
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from models import User

def invalid_credentials(form, field):
  """ Username and password checker """
  username_entered = form.username.data
  password_entered = field.data

 

  user_object = User.query.filter_by(username=username_entered).first()
  if user_object is None:
    raise ValidationError("Username or password is incorrect")
  elif not pbkdf2_sha256.verify(password_entered, user_object.password):
    raise ValidationError("Username or password is incorrect")

class RegistrationForm(FlaskForm):
  """ Registration form """ 

  username = StringField('username_label', validators=[InputRequired(message="Username Required"), Length(min=3, message="Username must be at least 3 characters")])
  password = PasswordField('password_label', validators=[InputRequired(message="Password Required"), Length(min=8, message="Username must be at least 8 characters")])
  confirm_pswd = PasswordField('confirm_pswd_label', validators=[InputRequired(message="Password Required"), EqualTo('password', message="Passwords Must Match")])
  submit_button = SubmitField('Create')

  def validate_username(self, username):
    user_object = User.query.filter_by(username=username.data).first()
    if user_object:
      raise ValidationError("Oops! Someone has already taken this username!")

class LoginForm(FlaskForm):
  """ Login form """
  username = StringField('username_label', validators=[InputRequired(message="Username required")])
  password = PasswordField('password_label', validators=[InputRequired(message="Password required"), invalid_credentials])
  submit_button = SubmitField('Log in')