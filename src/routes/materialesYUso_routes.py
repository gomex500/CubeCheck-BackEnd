from flask import Blueprint, request, jsonify
from src.controllers.jwt import validar_token
from src.configs.conecction import collections
from src.controllers.materialesY_controllers import (
    insertar_materialY,
    obtener_materialY,
    obtener_material,
    eliminar_materialY,
    actualizar_materialY
    )

#inicializando rutas de usuario
materialyuso_routes = Blueprint('materialyuso_routes', __name__)

#validacion de token
@materialyuso_routes.before_request
def verificar_token():
    try:
        token = request.headers['Authorization'].split(" ")[1]
        validar_token(token, output=False)
    except:
        return jsonify({"Menssage":"Error de autenticacion, no estas autorizado"})

#ruta crear material y
@materialyuso_routes.route('/materialyuso', methods=['POST'])
def insertar_materialy_ruta():
    return insertar_materialY(collections('materiales_yUso'))

#ruta mostrar materiales x
@materialyuso_routes.route('/materialyuso', methods=['GET'])
def obtener_materialy_ruta():
    return obtener_materialY(collections('materiales_yUso'))

#ruta mostrar usuario
@materialyuso_routes.route('/materialyuso/<id>', methods=['GET'])
def obtener_material_ruta(id):
    return obtener_material(collections('materiales_yUso'), id)

#ruta eliminar usuario
@materialyuso_routes.route('/materialyuso/<id>', methods=['DELETE'])
def eliminar_materialy_ruta(id):
    return eliminar_materialY(collections('materiales_yUso'), id)

#ruta actualizar usuario
@materialyuso_routes.route('/materialyuso/<id>', methods=['PUT'])
def actualizar_materialy_ruta(id):
    return actualizar_materialY(collections('materiales_yUso'), id)