from flask import Blueprint, request
from src.controllers.jwt import validar_token

home = Blueprint('home', __name__)

@home.route('/')
def index():
    return 'hola mundo'

@home.route('/token')
def verificar():
    token = request.headers['Authorization'].split(" ")[1]
    return validar_token(token, output=True)