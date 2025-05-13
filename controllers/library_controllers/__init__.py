from flask import Blueprint

library = Blueprint('library', __name__)

from .add_assets_routes import *
from .assets_list_routes import *
