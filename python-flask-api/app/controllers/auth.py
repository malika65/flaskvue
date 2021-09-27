from flask import Blueprint, redirect, url_for, render_template
from app import *
from flask_jwt_extended import create_access_token, decode_token
from ..models.user import *


auth_blueprint = Blueprint('index', __name__)


json = UserJsonSchema()
json_list = UserJsonSchema(many=True)


# Return user login data
def login_user(user):
    user_id = user.id
    expires = timedelta(minutes=120)
    token = create_access_token(identity=user_id, expires_delta=expires)
    return jsonify(dict(token=token, user=json.dump(user)))


# Authenticate and login user
@auth_blueprint.route('/login', methods=['POST'])
def login():
    try:
        username = request.body['username']
        password = request.body['password']
        query = User.query
        query = query.filter((User.name == username) | (User.email == username))
        user = query.first()
        try:
            if not user or not utils.check_password(user.password, password):
                return jsonify("Username or password not correct"), 400
        except Exception as ex:
            return jsonify("Username or password not correct"), 400 # password check failed
        return login_user(user)
    except Exception as ex:
        return abort(500, str(ex))


# Save new user record
@auth_blueprint.route('/register', methods=['POST'])
def register():
    try:
        modeldata = request.body
        form = UserRegisterForm(modeldata)
        errors = [] # form validation errors
        
        # validate register form data
        if not form.validate():
            errors.append(form.errors)
        
        if errors:
            return jsonify(errors), 400
        
        record = User()
        form.populate_obj(record)
        record.password = utils.hash_password(modeldata['password'])
        # check if name record already exist in the database
        rec_value = str(modeldata['name'])
        rec_exist = utils.is_unique(User, "name", rec_value)
        if rec_exist:
            return jsonify(rec_value + " Already exist!"), 400
        # check if email record already exist in the database
        rec_value = str(modeldata['email'])
        rec_exist = utils.is_unique(User, "email", rec_value)
        if rec_exist:
            return jsonify(rec_value + " Already exist!"), 400
        
        # save user records
        db.session.add(record)
        db.session.commit()
        db.session.flush()
        rec_id = record.id
        return login_user(record)
    except Exception as ex:
        return abort(500, str(ex))


# send password reset link to user email
@auth_blueprint.route('/forgotpassword', methods=['POST'])
def forgotpassword():
    try:
        modeldata = request.body
        email = modeldata['email']
        user = User.query.filter(User.email == email).first()
        if user:
            user_id = user.id
            expires = timedelta(hours=1)
            token = create_access_token(identity = user_id, expires_delta=expires)
            resetlink = app.config['FRONTEND_ADDR'] + "/#/index/resetpassword?token=" + token
            username = user.name
            mailsubject = 'Password Reset'
            template_context = dict(pagetitle='Password reset', username=username, email=email, resetlink = resetlink)
            mailbody = render_template('pages/passwordmanager/password_reset_email_template.html', **template_context)
            response = utils.send_mail(email, mailsubject, mailbody)
            return "We have emailed your password reset link!"
        else:
            return jsonify("The email address is not registered on the system"), 400
    except Exception as ex:
            return abort(500, str(ex))


# Reset user password
@auth_blueprint.route('/resetpassword', methods=['POST'])
def resetpassword():
    try:
        modeldata = request.body
        token = modeldata['token']
        payload = decode_token(token)
        if payload:
            user_id = payload['identity']
            form = PasswordForm(modeldata)
            if form.validate():
                record = User.query.filter_by(id=user_id).first_or_404()
                record.password = utils.hash_password(form.password.data)
                db.session.commit()
                return jsonify("Password changed")
            else:
                return jsonify(form.errors), 400
        else:
            return jsonify('The token is invalid or has expired'), 422
    except Exception as ex:
        return abort(500, str(ex))
