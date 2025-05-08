from flask import Blueprint

course = Blueprint('course', __name__)

from .add_course_routes import *
from .course_list_routes import *
from .add_subject_routes import *
