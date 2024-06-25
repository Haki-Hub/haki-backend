from flask import Blueprint, jsonify
from app.services.wagtail_service import get_wagtail_pages

bp = Blueprint('wagtail', __name__)

@bp.route('/pages/')
def wagtail_pages():
    response = get_wagtail_pages()
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch data from Wagtail API"}), response.status_code
