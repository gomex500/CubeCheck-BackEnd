from flask import Blueprint
from src.configs.conecction import collections
from src.controllers.login_controllers import signin, login

#inicializando ruta login y registro
login_routes = Blueprint('login_routes', __name__)

#ruta de logeo de usuario
@login_routes.route('/login', methods=['POST'])
def login_route():
    return login(collections('usuarios'))

#ruta de registro de usuarios
@login_routes.route('/signin', methods=['POST'])
def signin_route():
    return signin(collections('usuarios'))