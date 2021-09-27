from flask import Blueprint, render_template
from app import *


home_blueprint = Blueprint('home', __name__)


@home_blueprint.route('/')
@home_blueprint.route('/index')
@jwt_required
def home():
    return render_template('pages/home/index.html')
