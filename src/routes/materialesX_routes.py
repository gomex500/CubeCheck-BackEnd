from flask import Blueprint, request, jsonify
from src.controllers.jwt import validar_token
from src.configs.conecction import collections
from src.controllers.materialesX_controllers import (
    insertar_materialX,
    obtener_materialX,
    obtener_material,
    eliminar_materialx,
    actualizar_materialx,
    obtener_mis_materialX
    )

#inicializando rutas de usuario
materialx_routes = Blueprint('materialx_routes', __name__)

#validacion de token
@materialx_routes.before_request
def verificar_token():
    try:
        token = request.headers['Authorization'].split(" ")[1]
        validar_token(token, output=False)
    except:
        return jsonify({"Menssage":"Error de autenticacion, no estas autorizado"})

#ruta crear material x
@materialx_routes.route('/materialx', methods=['POST'])
def insertar_materialx_ruta():
    return insertar_materialX(collections('materiales_x'))

#ruta mostrar materiales x
@materialx_routes.route('/materialx', methods=['GET'])
def obtener_materialx_ruta():
    return obtener_materialX(collections('materiales_x'))

#ruta mostrar usuario
@materialx_routes.route('/materialx/<id>', methods=['GET'])
def obtener_material_ruta(id):
    return obtener_material(collections('materiales_x'), id)

#ruta eliminar usuario
@materialx_routes.route('/materialx/<id>', methods=['DELETE'])
def eliminar_materialx_ruta(id):
    return eliminar_materialx(collections('materiales_x'), id)

#ruta actualizar usuario
@materialx_routes.route('/materialx/<id>', methods=['PUT'])
def actualizar_materialx_ruta(id):
    return actualizar_materialx(collections('materiales_x'), id)

#ruta actualizar usuario
@materialx_routes.route('/mismaterialx/<user>', methods=['GET'])
def obtener_mismaterialx_ruta(user):
    return obtener_mis_materialX(collections('materiales_x'), user)