from flask import Blueprint, jsonify, abort, request
from ..models import Website, db

bp = Blueprint('website', __name__, url_prefix='/website')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    websites = Website.query.all()  # ORM performs SELECT query
    result = []
    for w in websites:
        result.append(w.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    w = Website.query.get_or_404(id)
    return jsonify(w.serialize())


@bp.route('', methods=['POST'])
def create():
    w = Website(
        id=request.json['id'],
        name=request.json['name'],
        niche=request.json['niche']
    )
    db.session.add(w)
    db.session.commit()
    return jsonify(w.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    w = Website.query.get_or_404(id)
    try:
        db.session.delete(w)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong
        return jsonify(False)


@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id):
    w = Website.query.get_or_404(id)
    if "name" not in request.json:
        return abort(400)
    else:
        w.name = request.json['name']
        w.niche = request.json['niche']
    try:
        db.session.commit()
        return jsonify(w.serialize())
    except:
        return jsonify(False)
