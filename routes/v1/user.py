from flask import Blueprint
from controllers.UserController import findAll

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET']) ( findAll )