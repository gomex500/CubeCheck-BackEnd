from datetime import datetime
from flask import request, jsonify
from bson import ObjectId
from src.models.user_models import UserModel
from src.controllers.jwt import crear_token
import json

def insertar_usuario(collections):
    data = json.loads(request.data)
    user_instance = UserModel(data)
    id = collections.insert_one(user_instance.__dict__).inserted_id
    token = crear_token(data=request.json)
    return jsonify({'id':str(id), "token":token.decode('utf-8')})

def obtener_usuarios(collections):
    users = []
    for doc in collections.find():
        user = UserModel(doc).__dict__
        user['_id'] = str(doc['_id'])
        users.append(user)
    return jsonify(users)

def obtener_usuario(collections, id):
    doc = collections.find_one({'_id': ObjectId(id)})
    user_data = UserModel(doc).__dict__
    user_data['_id'] = str(doc['_id'])
    return jsonify(user_data)

def eliminar_usuario(collections, id):
    collections.delete_one({'_id': ObjectId(id)})
    return jsonify({'mensaje': 'Usuario eliminado'})

def actualizar_usuario(collections, id):
    user_data = collections.find_one({'_id': ObjectId(id)})
    user_data_update = UserModel(request.json)
    user_data_update.create_at = user_data['create_at']
    user_data_update.update_at = datetime.now()
    collections.update_one({'_id': ObjectId(id)}, {"$set": user_data_update.__dict__})
    return jsonify({'message': 'Usuario actualizado'})

