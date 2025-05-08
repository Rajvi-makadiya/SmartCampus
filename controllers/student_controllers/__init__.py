from flask import Blueprint

student = Blueprint('student', __name__)

from .student_list_routes import *
from .add_student_routes import *
