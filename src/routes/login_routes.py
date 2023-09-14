from flask import Blueprint
from src.configs.conecction import collections
from src.controllers.login_controllers import signin

login_routes = Blueprint('login_routes', __name__)

@login_routes.route('/login', methods=['POST'])
def login():
    pass

@login_routes.route('/signin', methods=['POST'])
def signin_route():
    return signin(collections('usuarios'))