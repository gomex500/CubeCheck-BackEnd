from datetime import datetime
from flask import request, jsonify
from bson import ObjectId
from src.models.materialesX_model import MateXModel
import json

#controlador insertar Material x en uso
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

#controlador mostrar materiales x en uso
def obtener_materialX(collections):
    try:
        materiales = []
        for doc in collections.find():
            material = MateXModel(doc).__dict__
            material['_id'] = str(doc['_id'])
            materiales.append(material)
        return jsonify(materiales)
    except Exception as e:
        response = jsonify({"message": "Error de petición", "error": str(e)})
        response.status_code = 500
        return response

#controlador mostrar material x en uso
def obtener_material(collections, id):
    try:
        doc = collections.find_one({'_id': ObjectId(id)})
        mate_data = MateXModel(doc).__dict__
        mate_data['_id'] = str(doc['_id'])
        return jsonify(mate_data)
    except:
        response = jsonify({"menssage":"error de peticion"})
        response.status = 401
        return response

#controlador eliminar material en uso
def eliminar_materialx(collections, id):
    try:
        collections.delete_one({'_id': ObjectId(id)})
        return jsonify({'mensaje': 'Material eliminado'})
    except:
        response = jsonify({"menssage":"Error al Eliminar"})
        response.status = 401
        return response

#controlador actualizar material
def actualizar_materialx(collections, id):
    try:
        mate_data = collections.find_one({'_id': ObjectId(id)})
        mate_data_update = MateXModel(request.json)

        #insertando datos sencibles
        mate_data_update.create_at = mate_data['create_at']
        mate_data_update.update_at = datetime.now()
        collections.update_one({'_id': ObjectId(id)}, {"$set": mate_data_update.__dict__})
        return jsonify({"message": "Material actualizado"})
    except:
        response = jsonify({"menssage":"error de peticion"})
        response.status = 401
        return response