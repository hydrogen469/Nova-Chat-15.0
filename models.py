from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

db = SQLAlchemy()

class User(db.Model):
  """ User model """
__tablename__ = "users"
id = db.Column(db.Integer, primary_key=True)
username = db.Column(db.String(25), unique=True, nullable=False)
password = db.Column(db.String(), nullable=False)

