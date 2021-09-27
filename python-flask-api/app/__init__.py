from flask import Flask, request, jsonify, abort, render_template
from flask_sqlalchemy import SQLAlchemy, BaseQuery
from sqlalchemy import func, text, literal_column, cast
from flask_marshmallow import Marshmallow
from .helpers import jsonmultidict as json2dict
from .helpers.json_encoder import CustomJSONEncoder
from flask_mail import Mail
from flask_cors import CORS
from datetime import datetime, date, time, timedelta
import os
import flask_excel as excel
from flask_jwt_extended import JWTManager, jwt_required, current_user
app = Flask(__name__)
# Load the configuration from the instance folder
app.config.from_pyfile('config.py')
app.url_map.strict_slashes = False
CORS(app)  # This will enable CORS for all routes
MAX_RECORD_COUNT = app.config['MAX_RECORD_COUNT']
ORDER_TYPE = app.config['ORDER_TYPE']
SITE_NAME = app.config['SITE_NAME']
DEBUG = app.config['DEBUG']

db = SQLAlchemy(app)  # init database
ma = Marshmallow(app)  # init marshmallow for json decoding
from flask_babel import Babel, gettext, ngettext
babel = Babel(app)
@babel.localeselector
def get_locale():
    if 'locale' in session:
        return session['locale']
    else:
        return g.get('lang_code', app.config['BABEL_DEFAULT_LOCALE'])
@babel.timezoneselector
def get_timezone():
    user = g.get('user', None)
    if user is not None:
        return user.timezone
@app.route('/change_language/<lang>')
def change_language(lang = None):
    if lang :
        session['locale'] = lang
        locale = lang
        flash('Language Changed to ' + app.config['LANGUAGES'][locale], 'success')
    rurl = request.args.get('redirect', '/index')
    return redirect(rurl)

mail = Mail(app)  # init mail client
excel.init_excel(app)  # init flask_excel


from .helpers.utils import utils, OptionalButNotEmpty

# Handle app exceptions
# Return 500 Internal Server Error
@app.errorhandler(500)
def server_error(msg):
    if DEBUG:
        return jsonify(str(msg)), 500 # return exception message in development mode
    else:
        print("\n" + str(msg) + "\n")
        return jsonify("Error processing request..."), 500

def resolve_request_body():
    # Before every request, resolve `request.body` from `request.get_json()`
    if request.method == 'POST':
        body = request.get_json()
        if body:
            if isinstance(body, list):
                allpost = []
                for post in body:
                    allpost.append(json2dict.get_json_multidict(post))
                request.body = allpost
            else:
                request.body = json2dict.get_json_multidict(body)
        else:
            request.body = request.form

app.before_request(resolve_request_body)
app.json_encoder = CustomJSONEncoder

jwt = JWTManager(app)


@jwt.user_loader_callback_loader
def user_loader_callback(identity):
    try:
        from .models.user import User
        user = User.query.filter(User.id == identity).first()
        return user
    except Exception as ex:
        print(str(ex))
        return None


@jwt.invalid_token_loader
def invalid_token_callback(token):
    return jsonify("Invalid Token"), 401


from .controllers.components_data import  components_data_blueprint
from .controllers.fileuploader import file_uploader_blueprint
from .controllers.auth import auth_blueprint
from .controllers.account import account_blueprint
from .controllers.user import User_blueprint
from .controllers.blacklist import Blacklist_blueprint


# Page controller blueprint
app.register_blueprint(auth_blueprint, url_prefix = "/api/auth")
app.register_blueprint(account_blueprint, url_prefix = "/api/account")
app.register_blueprint(components_data_blueprint, url_prefix = "/api/components_data")
app.register_blueprint(file_uploader_blueprint, url_prefix = "/api/fileuploader")
app.register_blueprint(User_blueprint, url_prefix = "/api/user")
app.register_blueprint(Blacklist_blueprint, url_prefix = "/api/blacklist")