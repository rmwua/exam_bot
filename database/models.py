from peewee import (
    Model,
    CharField,
    IntegerField,
    ForeignKeyField,
    AutoField, SqliteDatabase
)

db = SqliteDatabase("/Users/polly/Desktop/test_umschool/database.db")


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    student_id = AutoField(primary_key=True)
    user_id = IntegerField()  # telegram user id
    name = CharField()
    surname = CharField()


class Scores(BaseModel):
    score_id = AutoField(primary_key=True)
    student_id = ForeignKeyField(model=User, backref='results')
    user_id = IntegerField()
    module_name = CharField()
    score = CharField()


class LoggedUsers(BaseModel):
    student_id = ForeignKeyField(model=User, primary_key=True)  # telegram user id
    user_id = IntegerField(User)
    name = CharField()
    surname = CharField()


class Modules(BaseModel):
    module_list = []


def create_models():
    db.create_tables(BaseModel.__subclasses__())

