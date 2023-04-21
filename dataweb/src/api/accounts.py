from flask import Blueprint, jsonify, abort, request
from ..models import Account, db

bp = Blueprint('account', __name__, url_prefix='/account')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    account = Account.query.all()  # ORM performs SELECT query
    result = []
    for a in account:
        result.append(a.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response
