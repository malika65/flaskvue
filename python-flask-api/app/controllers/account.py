from flask import Blueprint
from app import *
from ..models.user import *


account_blueprint = Blueprint('account', __name__)


json = UserJsonSchema()
json_list = UserJsonSchema(many=True)


# View user account detail
@account_blueprint.route('/')
@account_blueprint.route('/index')
@jwt_required
def view():
    try:
        rec_id = current_user.id
        query = User.query.filter(User.id == rec_id)
        query = query.with_entities(
            User.name,
            User.id,
            User.email
        )
        
        record = query.first()
        if not record:
            return jsonify("No record found"), 404
        return json.jsonify(record)
    except Exception as ex:
        return abort(500, str(ex))


# Update user account detail
@account_blueprint.route('/edit', methods=['GET', 'POST'])
@jwt_required
def edit():
    try:
        rec_id = current_user.id
        record = User.query.filter(User.id == rec_id).first()
        if not record:
            return jsonify("No record found"), 404
        
        if request.method == 'POST':
            modeldata = request.body
            errors = []
            form = UserAccountEditForm(modeldata, obj=record)
            
            if not form.validate():
                errors.append(form.errors)
            
            if errors:
                return jsonify(errors), 400
            
            # save User record
            form.populate_obj(record)
            db.session.commit()
        return json.jsonify(record)
    except Exception as ex:
        return abort(500, str(ex))


@account_blueprint.route('/currentuserdata')
@jwt_required
def currentuserdata():
    user = json.dump(current_user)
    del user['password']
    return jsonify(user)


# Change user password
@account_blueprint.route('/changepassword', methods=['POST'])
@jwt_required
def changepassword():
    try:
        modeldata = request.body
        form = ChangePasswordForm(modeldata)
        if not form.validate():
            return jsonify(form.errors), 400
        user = User.query.filter(User.id == current_user.id).first()
        current_password = modeldata['oldpassword']
        if not utils.check_password(user.password, current_password):
            return jsonify("Current password is incorrect"), 400
        user.password = utils.hash_password(modeldata['newpassword'])
        db.session.commit()
        return jsonify("Password change completed")
    except Exception as ex:
        return abort(500, str(ex))
