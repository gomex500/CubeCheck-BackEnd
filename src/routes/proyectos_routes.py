from flask import Blueprint, request, jsonify
from src.controllers.jwt import validar_token
from src.configs.conecction import collections
from src.controllers.proyectos_controllers import (
    insertar_proyecto,
    obtener_proyecto,
    obtener_proyectos,
    actualizar_proyecto,
    eliminar_proyecto
)

#inicializando rutas de usuario
proyectos_routes = Blueprint('proyectos_routes', __name__)

#validacion de token
@proyectos_routes.before_request
def verificar_token():
    try:
        token = request.headers['Authorization'].split(" ")[1]
        validar_token(token, output=False)
    except:
        return jsonify({"Menssage":"Error de autenticacion, no estas autorizado"})

#ruta crear material x
@proyectos_routes.route('/proyectos', methods=['POST'])
def insertar_proyectos_ruta():
    return insertar_proyecto(collections('proyectos'))

#ruta mostrar materiales x
@proyectos_routes.route('/proyecto/<user>', methods=['GET'])
def obtener_proyectos_ruta(user):
    return obtener_proyectos(collections('proyectos'), user)

#ruta mostrar usuario
@proyectos_routes.route('/proyectos/<id>', methods=['GET'])
def obtener_proyectos_id_ruta(id):
    return obtener_proyecto(collections('proyectos'), id)

#ruta eliminar usuario
@proyectos_routes.route('/proyectos/<id>', methods=['DELETE'])
def eliminar_proyectos_ruta(id):
    return eliminar_proyecto(collections('proyectos'), id)

#ruta actualizar usuario
@proyectos_routes.route('/proyectos/<id>', methods=['PUT'])
def actualizar_proyectos_ruta(id):
    return actualizar_proyecto(collections('proyectos'), collections('materiales_x'), collections('materiales_y'), id)
