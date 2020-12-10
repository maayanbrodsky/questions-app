from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
app= Flask(__name__)

# test

db = SQLAlchemy(app)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    textbook = db.Column(db.String(100), unique=True, nullable=False)
    chapter = db.Column(db.Integer, nullable=False)
    section = db.Column(db.String(100), nullable=True)

    #topic = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"""#{self.id}, {self.textbook}, chapter: {self.chapter}, 
                   section: {self.section}"""


class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


# app = Flask(__name__)
# app.config.from_pyfile('config.py')


# db = PostgresqlDatabase(
#         'test1',  # Required by Peewee.
#         user='postgres',  # Will be passed directly to psycopg2.
#         password='Agent99',  # Ditto.
#     )

# SECRET_KEY = "SECRET_KEY"
# print(os.environ)

# db = PostgresqlDatabase(
#     config('DATABASE'),
#     user=config('USER'),
#     password=config('PASSWORD'),
#     host=config('HOST'),
#     port=config('PORT'),
# )
#

# db = PostgresqlDatabase(
#     os.getenv('DATABASE'),
#     user=os.getenv('USER'),
#     password=os.getenv('PASSWORD'),
#     host=os.getenv('HOST'),
#     port=os.getenv('PORT'),
# )

