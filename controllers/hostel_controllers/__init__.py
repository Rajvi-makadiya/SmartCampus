from flask import Blueprint

hostel = Blueprint('hostel', __name__)

from .room_list_routes import *
from .room_type_routes import *
