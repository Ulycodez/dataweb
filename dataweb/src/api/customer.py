from flask import Blueprint, jsonify, abort, request
from ..models import Customer, db

bp = Blueprint('customer', __name__, url_prefix='/customer')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    customers = Customer.query.all()  # ORM performs SELECT query
    result = []
    for c in customers:
        result.append(c.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    c = Customer.query.get_or_404(id)
    return jsonify(c.serialize())


@bp.route('', methods=['POST'])
def create():
    c = Customer(
        id=request.json['id'],
        first_name=request.json['first_name'],
        last_name=request.json['last_name'],
        website_id=request.json['website_id'],
        account_id=request.json['account_id']
    )
    db.session.add(c)
    db.session.commit()
    return jsonify(c.serialize())


@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id):
    c = Customer.query.get_or_404(id)
    if "customer" not in request.json:
        return abort(400)
    else:
        c.account_id = request.json['account_id']
        c.first_name = request.json['first_name']
        c.id = request.json['id']
        c.last_name = request.json['last_name']
        c.website_id = request.json['website']
    try:
        db.session.commit()
        return jsonify(c.serialize())
    except:
        return jsonify(False)
