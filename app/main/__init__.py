# blueprint because there is no current_app to use, so flask
# gives the blueprint solution
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
