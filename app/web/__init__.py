from flask import Blueprint

web = Blueprint("web", __name__)

from app.web import book, auth,gift
