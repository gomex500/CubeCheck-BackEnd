from datetime import datetime
from urllib import response
from flask import request, jsonify
from bson import ObjectId
from src.models.user_models import UserModel
from src.controllers.jwt import crear_token
import json

#controlador insertar usuario
def insertar_usuario(collections):
    try:
        data = json.loads(request.data)
        user_instance = UserModel(data)
        id = collections.insert_one(user_instance.__dict__).inserted_id
        token = crear_token(data=request.json)
        return jsonify({'id':str(id), "token":token.decode('utf-8')})
    except:
        response = jsonify({"menssage","error de ingreso"})
        response.status = 400
        return response

#controlador mostrar usuarios
def obtener_usuarios(collections):
    try:
        users = []
        for doc in collections.find():
            user = UserModel(doc).__dict__
            user['_id'] = str(doc['_id'])
            users.append(user)
        return jsonify(users)
    except:
        response = jsonify({"menssage","error de peticion"})
        response.status = 401
        return response

#controlador mostrar usuario
def obtener_usuario(collections, id):
    try:
        doc = collections.find_one({'_id': ObjectId(id)})
        user_data = UserModel(doc).__dict__
        user_data['_id'] = str(doc['_id'])
        return jsonify(user_data)
    except:
        response = jsonify({"menssage","error de peticion"})
        response.status = 401
        return response

#controlador eliminar usuario
def eliminar_usuario(collections, id):
    try:
        collections.delete_one({'_id': ObjectId(id)})
        return jsonify({'mensaje': 'Usuario eliminado'})
    except:
        response = jsonify({"menssage","error de peticion"})
        response.status = 401
        return response

#controlador actualizar usuario
def actualizar_usuario(collections, id):
    try:
        user_data = collections.find_one({'_id': ObjectId(id)})
        user_data_update = UserModel(request.json)
        user_data_update.create_at = user_data['create_at']
        user_data_update.update_at = datetime.now()
        collections.update_one({'_id': ObjectId(id)}, {"$set": user_data_update.__dict__})
        return jsonify({'message': 'Usuario actualizado'})
    except:
        response = jsonify({"menssage","error de peticion"})
        response.status = 401
        return response
