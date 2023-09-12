from datetime import datetime
from flask import request, jsonify
from bson import ObjectId
from src.models.user_models import UserModel

def insertar_usuario(collections):
    id = collections.insert_one(UserModel(request.json)).inserted_id
    return jsonify(str(id))

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
