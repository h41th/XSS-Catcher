from flask import Blueprint

bp = Blueprint('api', __name__)

from app.api import xss, client, auth, user, x