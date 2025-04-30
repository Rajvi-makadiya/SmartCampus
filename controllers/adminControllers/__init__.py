from flask import Blueprint

admin = Blueprint('admin', __name__)

from .dashboard_routes import *