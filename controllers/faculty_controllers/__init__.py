from flask import Blueprint

faculty = Blueprint('faculty', __name__)

from .role_routes import *
from .faculty_list_routes import *
from .add_faculty_routes import *
from .faculty_timetable_routes import *