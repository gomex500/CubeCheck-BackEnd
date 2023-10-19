from datetime import datetime
from flask import request, jsonify
from bson import ObjectId
from src.models.materialesX_model import MateXModel
from src.controllers.jwt import crear_token
import json
import bcrypt

#controlador insertar Material x
def insertar_materialX(collections):
    try:
        data = json.loads(request.data)
        mate_instance = MateXModel(data)
        id = collections.insert_one(mate_instance.__dict__).inserted_id
        return jsonify({'id':str(id)})
    except Exception as e:
        response = jsonify({"message": "Error de petición", "error": str(e)})
        response.status_code = 500
        return response

#controlador mostrar materiales x
def obtener_materialX(collections):
    try:
        material = []
        for doc in collections.find():
            material = MateXModel(doc).__dict__
            material['_id'] = str(doc['_id'])

        return jsonify(material)
    except Exception as e:
        response = jsonify({"message": "Error de petición", "error": str(e)})
        response.status_code = 500
        return response