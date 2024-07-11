from flask import Blueprint

main = Blueprint('main', __name__)

from app.routes import main
from app.models import Category, Bill, Part, Section, Chapter
