from flask import Blueprint

staff = Blueprint('staff', __name__)

from .add_staff_routes import *
from .staff_list_routes import *
