from flask import Blueprint, request, jsonify
from src.controllers.jwt import validar_token
from src.configs.conecction import collections
from src.controllers.materialesX_controllers import (
    insertar_materialX,
    obtener_materialX,
    obtener_material,
    eliminar_materialx,
    actualizar_materialx
    )

#inicializando rutas de usuario
materialxuso_routes = Blueprint('materialxuso_routes', __name__)

#validacion de token
@materialxuso_routes.before_request
def verificar_token():
    try:
        token = request.headers['Authorization'].split(" ")[1]
        validar_token(token, output=False)
    except:
        return jsonify({"Menssage":"Error de autenticacion, no estas autorizado"})

#ruta crear material x
@materialxuso_routes.route('/materialxuso', methods=['POST'])
def insertar_materialx_ruta():
    return insertar_materialX(collections('materiales_xUso'))

#ruta mostrar materiales x
@materialxuso_routes.route('/materialxuso', methods=['GET'])
def obtener_materialx_ruta():
    return obtener_materialX(collections('materiales_xUso'))

#ruta mostrar usuario
@materialxuso_routes.route('/materialxuso/<id>', methods=['GET'])
def obtener_material_ruta(id):
    return obtener_material(collections('materiales_xUso'), id)

#ruta eliminar usuario
@materialxuso_routes.route('/materialxuso/<id>', methods=['DELETE'])
def eliminar_materialx_ruta(id):
    return eliminar_materialx(collections('materiales_xUso'), id)

#ruta actualizar usuario
@materialxuso_routes.route('/materialxuso/<id>', methods=['PUT'])
def actualizar_materialx_ruta(id):
    return actualizar_materialx(collections('materiales_xUso'), id)