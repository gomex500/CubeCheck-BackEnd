from datetime import datetime
from flask import request, jsonify
from bson import ObjectId
from src.models.materialesY_model import MateYModel
import json

#controlador insertar Material y
def insertar_materialY(collections):
    try:
        data = json.loads(request.data)
        mate_instance = MateYModel(data)
        id = collections.insert_one(mate_instance.__dict__).inserted_id
        return jsonify({'id':str(id)})
    except Exception as e:
        response = jsonify({"message": "Error de petición", "error": str(e)})
        response.status_code = 500
        return response

#controlador mostrar materiales y
def obtener_materialY(collections):
    try:
        materiales = []
        for doc in collections.find():
            material = MateYModel(doc).__dict__
            material['_id'] = str(doc['_id'])
            materiales.append(material)
        return jsonify(materiales)
    except Exception as e:
        response = jsonify({"message": "Error de petición", "error": str(e)})
        response.status_code = 500
        return response

#controlador mostrar proyecto
def obtener_mis_materialY(collections, user):
    try:
        materiales = []
        for doc in collections.find({"user": user}):
            material = MateYModel(doc).__dict__
            material['_id'] = str(doc['_id'])
            materiales.append(material)
        return jsonify(materiales)
    except Exception as e:
        response = jsonify({"message": "Error de petición", "error": str(e)})
        response.status_code = 500
        return response

#controlador mostrar material
def obtener_material(collections, id):
    try:
        doc = collections.find_one({'_id': ObjectId(id)})
        mate_data = MateYModel(doc).__dict__
        mate_data['_id'] = str(doc['_id'])
        return jsonify(mate_data)
    except:
        response = jsonify({"menssage":"error de peticion"})
        response.status = 401
        return response

#controlador eliminar material y
def eliminar_materialY(collections, id):
    try:
        collections.delete_one({'_id': ObjectId(id)})
        return jsonify({'mensaje': 'Material eliminado'})
    except:
        response = jsonify({"menssage":"Error al Eliminar"})
        response.status = 401
        return response

#controlador actualizar material y
def actualizar_materialY(collections, id):
    try:
        mate_data = collections.find_one({'_id': ObjectId(id)})
        mate_data_update = MateYModel(request.json)

        #insertando datos sencibles
        mate_data_update.create_at = mate_data['create_at']
        mate_data_update.update_at = datetime.now()
        collections.update_one({'_id': ObjectId(id)}, {"$set": mate_data_update.__dict__})
        return jsonify({"message": "Material actualizado"})
    except:
        response = jsonify({"menssage":"error de peticion"})
        response.status = 401
        return response