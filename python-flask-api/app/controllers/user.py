from flask import Blueprint
from app import *
from ..models.user import *


User_blueprint = Blueprint('User', __name__)


json = UserJsonSchema()
json_list = UserJsonSchema(many=True)


# list User records
# @param fieldname: filter table records by a field
# @param fieldvalue:  filter value
# @request.args search: search records
# @request.args orderby: sort records by field name
# @request.args ordertype: sort type (asc|desc)
# @request.args page: current page number
# @request.args limit: maximum number of records to select
@User_blueprint.route('/')
@User_blueprint.route('/index')
@User_blueprint.route('/index/<fieldname>/<fieldvalue>')
@User_blueprint.route('/index/<fieldname>/<fieldvalue>')
@jwt_required
def index(fieldname=None, fieldvalue=None):
    try:
        query = User.query
        search = request.args.get('search')
        if search:
            query = query.filter(
                User.name.like(f'%{search}%') | 
                User.email.like(f'%{search}%') 
            )
        
        # filter by dynamic field name
        if fieldname:
            field_filter = text(f'{fieldname} = :fieldvalue').params(fieldvalue=fieldvalue)
            query = query.filter(field_filter)
        
        orderby = request.args.get('orderby')
        ordertype = request.args.get('ordertype', 'desc')
        if orderby:
            query = query.order_by(text(f'{orderby} {ordertype}'))
        else:
            query = query.order_by(text(f'User.id {ordertype}'))
        
        # fields to select
        query = query.with_entities(
            User.id,
            User.name,
            User.email
        )
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', MAX_RECORD_COUNT))
        offset = ((page-1) * limit)
        total_records = query.count()
        records = query.limit(limit).offset(offset).all()
        record_count = len(records)
        total_pages = round(total_records/limit)
        res = dict(
            records=json_list.dump(records), 
            total_records=total_records,
            record_count=record_count,
            total_pages=total_pages
        )
        return jsonify(res)
    except Exception as ex:
        return abort(500, str(ex))


# Select table record by ID
@User_blueprint.route('/<rec_id>')
@User_blueprint.route('/view/<rec_id>')
@jwt_required
def view(rec_id=None):
    try:
        query = User.query
        query = query.filter(User.id == rec_id)
        query = query.with_entities(
            User.id,
            User.name,
            User.email
        )
        
        record = query.first()
        if not record:
            return jsonify("No record found"), 404
        return json.jsonify(record)
    except Exception as ex:
        return abort(500, str(ex))


# Save form data to the User table
@User_blueprint.route('/add', methods=['POST'])
@jwt_required
def add():
    try:
        modeldata = request.body
        form = UserAddForm(modeldata)
        errors = [] # list of validation errors
        
        # validate user form data
        if not form.validate():
            errors.append(form.errors)
        
        if errors:
            return jsonify(errors), 400
        
        record = User()
        form.populate_obj(record)
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
        record.password = utils.hash_password(modeldata['password'])
        
        # save user records
        db.session.add(record)
        db.session.commit()
        db.session.flush()
        rec_id = record.id
        return json.jsonify(record)
    except Exception as ex:
        return abort(500, str(ex))


# Select record by table primary key and update with form data
@User_blueprint.route('/edit/<rec_id>', methods=['GET', 'POST'])
@jwt_required
def edit(rec_id=None):
    try:
        query = User.query
        query = query.filter(User.id == rec_id)
        record = query.first()
        if not record:
            return jsonify("No record found"), 404
        
        if request.method == 'POST':
            errors = []
            modeldata = request.body
            form = UserEditForm(modeldata, obj=record)
            
            if not form.validate():
                errors.append(form.errors)
            # check if name already exist in the database
            rec_value = str(modeldata['name'])
            rec_exist = utils.is_unique(User, "name", rec_value, "id", rec_id)
            if rec_exist:
                return jsonify(rec_value  + " Already exist!"), 400
            
            if errors:
                return jsonify(errors), 400
            
            # save User record
            form.populate_obj(record)
            db.session.commit()
        return json.jsonify(record)
    except Exception as ex:
        return abort(500, str(ex))


# Delete record from the database
# Support multi delete by separating record id by comma.
@User_blueprint.route('/delete/<rec_id>')
@jwt_required
def delete(rec_id):
    query = User.query
    arr_id = rec_id.split(',')
    try:
        query = query.filter(User.id.in_(arr_id))
        query.delete(synchronize_session=False)
        db.session.commit()
        return jsonify(arr_id)
    except Exception as ex:
        return abort(500, str(ex))
