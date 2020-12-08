from flask import Flask, render_template, url_for, redirect, request
from peewee import (ForeignKeyField, IntegerField, TextField, PostgresqlDatabase, Model)
from datetime import datetime

import config

app = Flask(__name__)
app.config.from_pyfile('config.py')


db = PostgresqlDatabase(
        'question_app_db',  # Required by Peewee.
        user='postgres',  # Will be passed directly to psycopg2.
        password='Agent99',  # Ditto.
    )


class BaseModel(Model):

    class Meta:
        database = db


class Topics(BaseModel):
    topic = TextField()

    class Meta:
        table_name = 'topics'


class Users(BaseModel):
    username = TextField()
    email = TextField()
    password = TextField()
    institution = TextField()

    class Meta:
        table_name = 'users'


class Questions(BaseModel):
    textbook = TextField()
    chapter = IntegerField()
    section = TextField()
    submitted_by = ForeignKeyField(Users)
    topic = ForeignKeyField(Topics)

    class Meta:
        table_name = 'questions'



TABLES = [Topics, Questions, Users]


with db.connection_context():
    db.create_tables(TABLES, safe=True)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        print('hello')


        return render_template('about.j2')
    else:
        return render_template('home.j2')


@app.route("/about", methods=['GET', 'POST'])
def about():
    return render_template('about.j2')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.j2')
    elif request.method == 'POST':
        details = dict(request.form)
        print(details)
        Users.create(username=details['username'],
                     password=details['password'],
                     email=details['email'],
                     institution=details['institution'])
        return render_template('about.j2')



if __name__ == '__main__':
    app.run()