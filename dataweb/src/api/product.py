from flask import Blueprint, jsonify, abort, request
from ..models import Product, db

bp = Blueprint('product', __name__, url_prefix='/product')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    products = Product.query.all()  # ORM performs SELECT query
    result = []
    for p in products:
        result.append(p.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response
