import json
import bcrypt
from flask import request, jsonify
from src.models.user_models import UserModel
from src.controllers.jwt import crear_token

#funcion para vilidar si el correo existe
def validacion_email(coll, email):
    doc = coll.find_one({'email': email})
    if doc:
        return True
    return False


#validar si el password existe
def validar_password(coll, password):
    passEncriptado = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    doc = coll.find_one({'password': passEncriptado})
    if doc:
        return True
    return False


#controllador de registro de usuarios
def signin(collections):
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
            "telefono": user_instance.telefono,
            "email": user_instance.email,
            "password": user_instance.password
        }
        token = crear_token(data=user_data)
        return jsonify({'id':str(id), "token":token.decode('utf-8')})
    except:
        response = jsonify({"menssage","error de registro"})
        response.status = 400
        return response


#controllador de logeo de usuarios
def login(collections):
    try:
        data = json.loads(request.data)
        user_instance = UserModel(data)

        # Validar si el correo electrónico existe
        if not validacion_email(collections, user_instance.email):
            response = jsonify({"message": "El correo electrónico no existe"})
            response.status_code = 401
            return response

        # Obtener el documento del usuario
        user_doc = collections.find_one({'email': user_instance.email})
        user_data = {
            "nombre": user_doc['nombre'],
            "apellido": user_doc['apellido'],
            "edad": user_doc['edad'],
            "telefono": user_doc['telefono'],
            "email": user_doc['email'],
            "password": user_doc['password']
        }
        # Validar la contraseña
        if not bcrypt.checkpw(user_instance.password.encode('utf-8'), user_doc['password'].encode('utf-8')):
            response = jsonify({"message": "La contraseña no es válida"})
            response.status_code = 401
            return response

        # Crear y enviar el token
        token = crear_token(data=user_data)
        return jsonify({'id': str(user_doc['_id']), "token": token.decode('utf-8')})
    except Exception as e:
        print(str(e))
        response = jsonify({"message": "Error de inicio de sesión"})
        response.status_code = 400
        return response


