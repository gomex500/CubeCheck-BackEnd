from flask import Blueprint, request, jsonify
from src.controllers.jwt import validar_token
from src.configs.conecction import collections
from src.controllers.herramientas_controllers import (
    cambiar_valor_herramienta,
    insertar_herramienta,
    obtener_herramientas
)

#inicializando rutas de usuario
herramienta_routes = Blueprint('herramienta_routes', __name__)

#validacion de token
@herramienta_routes.before_request
def verificar_token():
    try:
        token = request.headers['Authorization'].split(" ")[1]
        validar_token(token, output=False)
    except:
        return jsonify({"Menssage":"Error de autenticacion, no estas autorizado"})


#crear herramienta
@herramienta_routes.route('/tools', methods=['GET'])
def ver_tool():
    return obtener_herramientas(collections('herramientas'))

#crear herramienta
@herramienta_routes.route('/tools', methods=['POST'])
def crear_herramienta():
    return insertar_herramienta(collections('herramientas'))

#cambiar valor herramienta
@herramienta_routes.route('/tools/<tool>', methods=['PUT'])
def cambiar_valor(tool):
    return cambiar_valor_herramienta(collections('herramientas'),tool)