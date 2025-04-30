from flask import Blueprint

auth = Blueprint('auth', __name__)

from .auth_login_routes import *
from .forgot_password_routes import *