import json
import bcrypt
from flask import request, jsonify
from src.models.user_models import UserModel
from src.controllers.jwt import crear_token

def signin(collections):
    try:
        data = json.loads(request.data)
        user_instance = UserModel(data)
        #encriptando password
        password = user_instance.password.encode('utf-8')
        salt = bcrypt.gensalt()
        passEncriptado = bcrypt.hashpw(password, salt)
        user_instance.password = passEncriptado.decode('utf-8')
        #insertando password y usuario a la db
        id = collections.insert_one(user_instance.__dict__).inserted_id
        token = crear_token(data=request.json)
        return jsonify({'id':str(id), "token":token.decode('utf-8')})
    except:
        response = jsonify({"menssage","error de registro"})
        response.status = 400
        return response


def login(collections):
    pass

