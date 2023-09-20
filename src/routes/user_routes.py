from flask import Blueprint, request, jsonify
from src.controllers.jwt import validar_token
from src.configs.conecction import collections
from src.controllers.user_controllers import (
    actualizar_rol,
    insertar_usuario,
    obtener_email,
    obtener_usuarios,
    obtener_usuario,
    eliminar_usuario,
    actualizar_usuario,
    actualizar_userb
)

#inicializando rutas de usuario
user_routes = Blueprint('user_routes', __name__)

#validacion de token
@user_routes.before_request
def verificar_token():
    try:
        token = request.headers['Authorization'].split(" ")[1]
        validar_token(token, output=False)
    except:
        return jsonify({"Menssage":"Error de autenticacion, no estas autorizado"})


#ruta crear usuario
@user_routes.route('/users', methods=['POST'])
def insertar_usuario_ruta():
    return insertar_usuario(collections('usuarios'))

#ruta mostrar usuarios
@user_routes.route('/users', methods=['GET'])
def obtener_usuarios_ruta():
    return obtener_usuarios(collections('usuarios'))

#ruta mostrar usuario
@user_routes.route('/user/<id>', methods=['GET'])
def obtener_usuario_ruta(id):
    return obtener_usuario(collections('usuarios'), id)

#ruta mostrar usuario por el correo
@user_routes.route('/email/<email>', methods=['GET'])
def obtener_email_ruta(email):
    return obtener_email(collections('usuarios'), email)

#ruta eliminar usuario
@user_routes.route('/user/<id>', methods=['DELETE'])
def eliminar_usuario_ruta(id):
    return eliminar_usuario(collections('usuarios'), id)

#ruta actualizar usuario
@user_routes.route('/user/<id>', methods=['PUT'])
def actualizar_usuario_ruta(id):
    return actualizar_usuario(collections('usuarios'), id)

#ruta actualizar rol de usuario
@user_routes.route('/rol/<id>', methods=['PUT'])
def actualizar_rol_ruta(id):
    return actualizar_rol(collections('usuarios'), id)

#ruta actualizar usuario sin password
@user_routes.route('/userb/<id>', methods=['PUT'])
def actualizar_userb_ruta(id):
    return actualizar_userb(collections('usuarios'), id)