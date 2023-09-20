from flask import Blueprint, request
from src.controllers.jwt import validar_token

#inicializando ruta
home = Blueprint('home', __name__)

#ruta inicial
@home.route('/')
def index():
    return '<h1>welcome to api CubeCheck</h1>'

#ruta verificadora de token
@home.route('/token')
def verificar():
    token = request.headers['Authorization'].split(" ")[1]
    return validar_token(token, output=True)