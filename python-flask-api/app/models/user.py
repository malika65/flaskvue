from app import db, ma, OptionalButNotEmpty, datetime
from wtforms import Form, StringField, FloatField, IntegerField, BooleanField
from wtforms.validators import *
from marshmallow import fields


class User(db.Model):
    __tablename__ = 'User'
    name = db.Column("name", db.String)
    password = db.Column("password", db.String)
    email = db.Column("email", db.String)
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)

    def has_verified_email(self):
        if self.email_verified_at is None:
            return False
        return True

    def set_email_verified(self):
        self.email_verified_at = datetime.now()

    def get_id(self):
        return str(self.id)

    def get_name(self):
        return str(self.name)

    def get_role(self):
        return ''

    def get_email(self):
        return str(self.email)

    def get_photo(self):
        return ''

   
class UserJsonSchema(ma.Schema):
    name = fields.Str()
    password = fields.Str()
    email = fields.Str()
    id = fields.Int()


class PasswordForm(Form):
    confirm_password = StringField('Confirm password', [InputRequired()])
    password = StringField('New Password', [InputRequired(), EqualTo('confirm_password', message='Passwords confirmation does not match')])


class ChangePasswordForm(Form):
    oldpassword = StringField('Old password', [InputRequired()])
    confirmpassword = StringField('Confirm password', [InputRequired()])
    newpassword = StringField('New Password', [InputRequired(), EqualTo('confirmpassword', message='Passwords confirmation does not match')])


class UserRegisterForm(Form):
    name = StringField('Name', [InputRequired()])
    password = StringField('Password', [InputRequired()])
    confirm_password = StringField('Confirm password', [InputRequired(), EqualTo('password', message='Passwords confirmation does not match')])
    email = StringField('Email', [InputRequired(),Email()])


class UserAccountEditForm(Form):
    name = StringField('Name', [OptionalButNotEmpty()])


class UserAddForm(Form):
    name = StringField('Name', [InputRequired()])
    password = StringField('Password', [InputRequired()])
    confirm_password = StringField('Confirm password', [InputRequired(), EqualTo('password', message='Passwords confirmation does not match')])
    email = StringField('Email', [InputRequired(),Email()])


class UserEditForm(Form):
    name = StringField('Name', [OptionalButNotEmpty()])
