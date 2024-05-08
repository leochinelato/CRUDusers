from peewee import Model, CharField, TextField
from database.database import db

class User(Model):
    name = CharField()
    email = CharField()
    description = TextField()

    class Meta:
        database = db