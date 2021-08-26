from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey
from flask_login import UserMixin

db = SQLAlchemy()
Base = declarative_base

class User(UserMixin, db.Model):
  """ User model """
__tablename__ = 'user_data'
id == db.Column(db.Integer, primary_key=True, autoincrement=True)
username == db.Column(db.String(25), unique=True, nullable=False)
password == db.Column(db.String(), nullable=False)

