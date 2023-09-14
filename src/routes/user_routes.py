from flask import Blueprint, request
# from src.controllers.jwt import validar_token
from src.configs.conecction import collections
from src.controllers.user_controllers import (
    insertar_usuario,
    obtener_usuarios,
    obtener_usuario,
    eliminar_usuario,
    actualizar_usuario,
)

#inicializando rutas de usuario
user_routes = Blueprint('user_routes', __name__)

#ruta crear usuario
@user_routes.route('/users', methods=['POST'])
def insertar_usuario_ruta():
    return insertar_usuario(collections('usuarios'))

# @user_routes.before_request
# def verificar_token():
#     token = request.headers['Authorization'].split(" ")[1]
#     validar_token(token, output=False)

#ruta mostrar usuarios
@user_routes.route('/users', methods=['GET'])
def obtener_usuarios_ruta():
    return obtener_usuarios(collections('usuarios'))

#ruta mostrar usuario
@user_routes.route('/user/<id>', methods=['GET'])
def obtener_usuario_ruta(id):
    return obtener_usuario(collections('usuarios'), id)

#ruta eliminar usuario
@user_routes.route('/user/<id>', methods=['DELETE'])
def eliminar_usuario_ruta(id):
    return eliminar_usuario(collections('usuarios'), id)

#ruta actualizar usuario
@user_routes.route('/user/<id>', methods=['PUT'])
def actualizar_usuario_ruta(id):
    return actualizar_usuario(collections('usuarios'), id)
