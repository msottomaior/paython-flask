#from main_flask import db
#from main_flask import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(16), nullable=False)
    passwd = db.Column('pass', db.String(16), nullable=False)
    name = db.Column(db.String(255))
    address = db.Column(db.String(255))
    todos = db.relationship('Todo', backref='users', lazy=True)

class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
    from_date = db.Column(db.DateTime, nullable=False)
    task = db.Column(db.String(255), nullable=False)

    # def __init__(self, id=None, email=None, passwd=None, name=None, address=None):
    #     self.id = id
    #     self.email = email
    #     self.passwd = passwd
    #     self.name = name
    #     self.address = address

    
