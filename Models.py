from peewee import (ForeignKeyField, IntegerField, TextField, PostgresqlDatabase, Model)
from playhouse.db_url import connect
import os


db = connect(os.environ.get('DATABASE_URL'))


class BaseModel(Model):

    class Meta:
        database = db


class Topics(BaseModel):
    topic = TextField()

    class Meta:
        table_name = 'topics'


class Users(BaseModel):
    username = TextField(null=False, unique=True)
    email = TextField(null=False, unique=True)
    password = TextField(null=False)
    institution = TextField(null=False)

    class Meta:
        table_name = 'users'


class Questions(BaseModel):
    textbook = TextField()
    chapter = IntegerField()
    section = TextField()
    submitted_by = ForeignKeyField(Users)
    question_text = TextField(null=False)
    topic = ForeignKeyField(Topics)

    class Meta:
        table_name = 'questions'