from flask import Blueprint

team = Blueprint('team', __name__)

from .role_routes import *
from .team_list_routes import *
