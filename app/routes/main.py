from flask import Blueprint, jsonify

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    return jsonify(message='Welcome to Flask!')
