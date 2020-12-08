from flask import Flask, render_template, url_for, redirect, request
from peewee import (ForeignKeyField, IntegerField, TextField, PostgresqlDatabase, Model)
from datetime import datetime
import jinja2

import config

app = Flask(__name__)
app.config.from_pyfile('config.py')


db = PostgresqlDatabase(
        'questions1',  # Required by Peewee.
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


class Questions(BaseModel):
    textbook = TextField()
    chapter = IntegerField()
    section = TextField()
    # topic = ForeignKeyField(Topics)

    class Meta:
        table_name = 'questions'


TABLES = [Topics, Questions]

with db.connection_context():
    db.create_tables(TABLES, safe=True)

@app.route("/home")
def home():
    return render_template('home.j2')


@app.route("/about")
def about():
    return render_template('about.j2')




if __name__ == '__main__':
    app.run()