from flask import Blueprint
from app import *
from ..models.blacklist import *


Blacklist_blueprint = Blueprint('Blacklist', __name__)


json = BlacklistJsonSchema()
json_list = BlacklistJsonSchema(many=True)


# list Blacklist records
# @param fieldname: filter table records by a field
# @param fieldvalue:  filter value
# @request.args search: search records
# @request.args orderby: sort records by field name
# @request.args ordertype: sort type (asc|desc)
# @request.args page: current page number
# @request.args limit: maximum number of records to select
@Blacklist_blueprint.route('/')
@Blacklist_blueprint.route('/index')
@Blacklist_blueprint.route('/index/<fieldname>/<fieldvalue>')
@Blacklist_blueprint.route('/index/<fieldname>/<fieldvalue>')
@jwt_required
def index(fieldname=None, fieldvalue=None):
    try:
        query = Blacklist.query
        search = request.args.get('search')
        if search:
            query = query.filter(
                Blacklist.name.like(f'%{search}%') | 
                Blacklist.organization.like(f'%{search}%') 
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
            query = query.order_by(text(f'BlackList.id {ordertype}'))
        
        # fields to select
        query = query.with_entities(
            Blacklist.id,
            Blacklist.name,
            Blacklist.organization,
            Blacklist.reiting
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
@Blacklist_blueprint.route('/<rec_id>')
@Blacklist_blueprint.route('/view/<rec_id>')
@jwt_required
def view(rec_id=None):
    try:
        query = Blacklist.query
        query = query.filter(Blacklist.id == rec_id)
        query = query.with_entities(
            Blacklist.id,
            Blacklist.name,
            Blacklist.organization,
            Blacklist.description,
            Blacklist.sum,
            Blacklist.reiting
        )
        
        record = query.first()
        if not record:
            return jsonify("No record found"), 404
        return json.jsonify(record)
    except Exception as ex:
        return abort(500, str(ex))


# Save form data to the Blacklist table
@Blacklist_blueprint.route('/add', methods=['POST'])
@jwt_required
def add():
    try:
        modeldata = request.body
        form = BlacklistAddForm(modeldata)
        errors = [] # list of validation errors
        
        # validate blacklist form data
        if not form.validate():
            errors.append(form.errors)
        
        if errors:
            return jsonify(errors), 400
        
        record = Blacklist()
        form.populate_obj(record)
        
        # save blacklist records
        db.session.add(record)
        db.session.commit()
        db.session.flush()
        rec_id = record.id
        return json.jsonify(record)
    except Exception as ex:
        return abort(500, str(ex))


# Select record by table primary key and update with form data
@Blacklist_blueprint.route('/edit/<rec_id>', methods=['GET', 'POST'])
@jwt_required
def edit(rec_id=None):
    try:
        query = Blacklist.query
        query = query.filter(Blacklist.id == rec_id)
        record = query.first()
        if not record:
            return jsonify("No record found"), 404
        
        if request.method == 'POST':
            errors = []
            modeldata = request.body
            form = BlacklistEditForm(modeldata, obj=record)
            
            if not form.validate():
                errors.append(form.errors)
            
            if errors:
                return jsonify(errors), 400
            
            # save Blacklist record
            form.populate_obj(record)
            db.session.commit()
        return json.jsonify(record)
    except Exception as ex:
        return abort(500, str(ex))


# Delete record from the database
# Support multi delete by separating record id by comma.
@Blacklist_blueprint.route('/delete/<rec_id>')
@jwt_required
def delete(rec_id):
    query = Blacklist.query
    arr_id = rec_id.split(',')
    try:
        query = query.filter(Blacklist.id.in_(arr_id))
        query.delete(synchronize_session=False)
        db.session.commit()
        return jsonify(arr_id)
    except Exception as ex:
        return abort(500, str(ex))
