from app import db, ma, OptionalButNotEmpty, datetime
from wtforms import Form, StringField, FloatField, IntegerField, BooleanField
from wtforms.validators import *
from marshmallow import fields


class Blacklist(db.Model):
    __tablename__ = 'BlackList'
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("name", db.String)
    organization = db.Column("organization", db.String)
    description = db.Column("description", db.String)
    sum = db.Column("sum", db.String)
    reiting = db.Column("reiting", db.String)

   
class BlacklistJsonSchema(ma.Schema):
    id = fields.Int()
    name = fields.Str()
    organization = fields.Str()
    description = fields.Str()
    sum = fields.Str()
    reiting = fields.Str()


class BlacklistAddForm(Form):
    name = StringField('Name', [InputRequired()])
    organization = StringField('Organization', [InputRequired()])
    description = StringField('Description', [InputRequired()])
    sum = StringField('Sum', [InputRequired()])
    reiting = StringField('Reiting', [InputRequired()])


class BlacklistEditForm(Form):
    name = StringField('Name', [OptionalButNotEmpty()])
    organization = StringField('Organization', [OptionalButNotEmpty()])
    description = StringField('Description', [OptionalButNotEmpty()])
    sum = StringField('Sum', [OptionalButNotEmpty()])
    reiting = StringField('Reiting', [OptionalButNotEmpty()])
