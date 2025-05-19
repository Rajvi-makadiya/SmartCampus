from flask import Blueprint

transport = Blueprint('transport', __name__)

from .vehicle_list_routes import *
