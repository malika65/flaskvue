
from flask import Blueprint
from app import *
from marshmallow import fields


class LabelValueJsonSchema(ma.Schema):
    label = fields.Str()
    value = fields.Str()


json = LabelValueJsonSchema()
json_list = LabelValueJsonSchema(many = True)


components_data_blueprint = Blueprint('components_data', __name__)


from ..models.user import User


@components_data_blueprint.route('/user_name_exist/<value>')
def user_name_exist(value = None):
    try:
        exist = User.query.with_entities(User.name).filter(User.name == value).first()
        if exist:
            return jsonify("true")
        return jsonify("false")
    except Exception as ex:
        return abort(500, str(ex))


@components_data_blueprint.route('/user_email_exist/<value>')
def user_email_exist(value = None):
    try:
        exist = User.query.with_entities(User.email).filter(User.email == value).first()
        if exist:
            return jsonify("true")
        return jsonify("false")
    except Exception as ex:
        return abort(500, str(ex))
