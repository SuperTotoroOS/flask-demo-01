from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import auth
from app.web import user
from app.web import book

