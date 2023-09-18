from datetime import datetime
from flask import request, jsonify
from bson import ObjectId
from src.models.user_models import UserModel
from src.controllers.jwt import crear_token
import json
import bcrypt

#funcion para vilidar si el correo existe
def validacion_email(coll, email):
    doc = coll.find_one({'email': email})
    if doc:
        return True
    return False

#controlador insertar usuario
def insertar_usuario(collections):
    try:
        data = json.loads(request.data)
        user_instance = UserModel(data)

        # Verificar si el correo electrónico ya existe
        if validacion_email(collections, user_instance.email):
            response = jsonify({"message": "El correo electrónico ya está en uso"})
            response.status_code = 400
            return response

        #encriptando password
        password = user_instance.password.encode('utf-8')
        salt = bcrypt.gensalt()
        passEncriptado = bcrypt.hashpw(password, salt)
        user_instance.password = passEncriptado.decode('utf-8')

        #insertando password y usuario a la db
        id = collections.insert_one(user_instance.__dict__).inserted_id
        user_data = {
            "nombre": user_instance.nombre,
            "apellido": user_instance.apellido,
            "edad": user_instance.edad,
            "rol":user_instance.rol,
            "telefono": user_instance.telefono,
            "email": user_instance.email,
            "password": user_instance.password
        }
        token = crear_token(data=user_data)
        return jsonify({'id':str(id), "token":token.decode('utf-8')})
    except:
        response = jsonify({"menssage":"error de registro"})
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
        response = jsonify({"menssage":"error de peticion"})
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
        response = jsonify({"menssage":"error de peticion"})
        response.status = 401
        return response

#controlador mostrar usuario por email
def obtener_email(collections, email):
    try:
        doc = collections.find_one({'email': email})
        if doc:
            user_data = UserModel(doc).__dict__
            user_data['_id'] = str(doc['_id'])
            return jsonify(user_data)
        else:
            response = jsonify({"message": "Correo no existe"})
            response.status_code = 404
            return response
    except Exception as e:
        response = jsonify({"message": "Error al buscar usuario por correo", "error": str(e)})
        response.status_code = 500
        return response

#controlador eliminar usuario
def eliminar_usuario(collections, id):
    try:
        collections.delete_one({'_id': ObjectId(id)})
        return jsonify({'mensaje': 'Usuario eliminado'})
    except:
        response = jsonify({"menssage":"error de peticion"})
        response.status = 401
        return response

#controlador actualizar usuario
def actualizar_usuario(collections, id):
    try:
        user_data = collections.find_one({'_id': ObjectId(id)})
        user_data_update = UserModel(request.json)

        #encriptando password
        password = user_data_update.password.encode('utf-8')
        salt = bcrypt.gensalt()
        passEncriptado = bcrypt.hashpw(password, salt)

        #insertando datos sencibles
        user_data_update.create_at = user_data['create_at']
        user_data_update.update_at = datetime.now()
        user_data_update.password = passEncriptado.decode('utf-8')

        collections.update_one({'_id': ObjectId(id)}, {"$set": user_data_update.__dict__})
        return jsonify({"message": "usuario actualizado"})
    except:
        response = jsonify({"menssage":"error de peticion"})
        response.status = 401
        return response

# Controlador para actualizar el rol de un usuario
def actualizar_rol(collections, id):
    try:
        nuevo_rol = request.json.get('rol')
        print(request.json.get('rol'))
        roles_validos = ['admin', 'user']
        if nuevo_rol not in roles_validos:
            return jsonify({'message': 'Rol no válido'}), 400

        collections.update_one({'_id': ObjectId(id)}, {'$set': {'rol': nuevo_rol}})
        return jsonify({'message': 'Rol actualizado correctamente'}), 200

    except Exception as e:
        return jsonify({'message': 'Error al actualizar el rol', 'error': str(e)}), 500