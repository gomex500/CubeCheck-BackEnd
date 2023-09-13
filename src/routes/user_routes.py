from flask import Blueprint, request
from src.controllers.jwt import validar_token
from src.controllers.user_controllers import (
    insertar_usuario,
    obtener_usuarios,
    obtener_usuario,
    eliminar_usuario,
    actualizar_usuario,
)
from pymongo import MongoClient
from src.configs.config import MONGO_URI
# MONGO_URI = 'mongodb+srv://gomex:Cwte9rnFIzzurYg0@cluster0.6iifh2k.mongodb.net/?retryWrites=true&w=majority'

user_routes = Blueprint('user_routes', __name__)

client = MongoClient(MONGO_URI)
db = client['cubecheck']
collections = db['usuarios']

@user_routes.route('/users', methods=['POST'])
def insertar_usuario_ruta():
    return insertar_usuario(collections)

# @user_routes.before_request
# def verificar_token():
#     token = request.headers['Authorization'].split(" ")[1]
#     validar_token(token, output=False)

@user_routes.route('/users', methods=['GET'])
def obtener_usuarios_ruta():
    return obtener_usuarios(collections)

@user_routes.route('/user/<id>', methods=['GET'])
def obtener_usuario_ruta(id):
    return obtener_usuario(collections, id)

@user_routes.route('/user/<id>', methods=['DELETE'])
def eliminar_usuario_ruta(id):
    return eliminar_usuario(collections, id)

@user_routes.route('/user/<id>', methods=['PUT'])
def actualizar_usuario_ruta(id):
    return actualizar_usuario(collections, id)
