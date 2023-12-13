from flask import Blueprint, request, jsonify
from src.controllers.jwt import validar_token
from src.configs.conecction import collections
from src.controllers.materialesY_controllers import (
    insertar_materialY,
    obtener_materialY,
    obtener_material,
    eliminar_materialY,
    actualizar_materialY,
    obtener_mis_materialY
    )

#inicializando rutas de usuario
materialy_routes = Blueprint('materialy_routes', __name__)

#validacion de token
@materialy_routes.before_request
def verificar_token():
    try:
        token = request.headers['Authorization'].split(" ")[1]
        validar_token(token, output=False)
    except:
        return jsonify({"Menssage":"Error de autenticacion, no estas autorizado"})

#ruta crear material y
@materialy_routes.route('/materialy', methods=['POST'])
def insertar_materialy_ruta():
    return insertar_materialY(collections('materiales_y'))

#ruta mostrar materiales x
@materialy_routes.route('/materialy', methods=['GET'])
def obtener_materialy_ruta():
    return obtener_materialY(collections('materiales_y'))

#ruta mostrar usuario
@materialy_routes.route('/materialy/<id>', methods=['GET'])
def obtener_material_ruta(id):
    return obtener_material(collections('materiales_y'), id)

#ruta eliminar usuario
@materialy_routes.route('/materialy/<id>', methods=['DELETE'])
def eliminar_materialy_ruta(id):
    return eliminar_materialY(collections('materiales_y'), id)

#ruta actualizar usuario
@materialy_routes.route('/materialy/<id>', methods=['PUT'])
def actualizar_materialy_ruta(id):
    return actualizar_materialY(collections('materiales_y'), id)

@materialy_routes.route('/mismaterialy/<user>', methods=['GET'])
def obtener_misMaterialy_ruta(user):
    return obtener_mis_materialY(collections('materiales_y'), user)