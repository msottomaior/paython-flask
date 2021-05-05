# class Todo:

#     def __init__(self, id, user_id, from_date, task):
#         self.id = id
#         self.user_id = user_id
#         self.from_date = from_date
#         self.task = task
#from main_flask import db

# from main_flask import app
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy(app)

# class Todo(db.Model):

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
#         nullable=False)
#     from_date = db.Column(db.DateTime, nullable=False)
#     task = db.Column(db.String(255), nullable=False)