from datetime import datetime
from flask import request, jsonify
from bson import ObjectId
from src.models.proyectos_model import ProyectoModel
import json

#controlador insertar proyecto
def insertar_proyecto(collections):
    try:
        data = json.loads(request.data)
        proyecto_instance = ProyectoModel(data)
        id = collections.insert_one(proyecto_instance.__dict__).inserted_id
        return jsonify({'id':str(id)})
    except Exception as e:
        response = jsonify({"message": "Error de petición", "error": str(e)})
        response.status_code = 500
        return response

#controlador mostrar proyecto
def obtener_proyectos(collections):
    try:
        proyectos = []
        for doc in collections.find():
            proyecto = ProyectoModel(doc).__dict__
            proyecto['_id'] = str(doc['_id'])
            proyectos.append(proyecto)
        return jsonify(proyectos)
    except Exception as e:
        response = jsonify({"message": "Error de petición", "error": str(e)})
        response.status_code = 500
        return response

#controlador mostrar proyecto
def obtener_proyecto(collections, id):
    try:
        doc = collections.find_one({'_id': ObjectId(id)})
        proyecto_data = ProyectoModel(doc).__dict__
        proyecto_data['_id'] = str(doc['_id'])
        return jsonify(proyecto_data)
    except:
        response = jsonify({"menssage":"error de peticion"})
        response.status = 401
        return response

#controlador eliminar proyecto
def eliminar_proyecto(collections, id):
    try:
        collections.delete_one({'_id': ObjectId(id)})
        return jsonify({'mensaje': 'Proyecto eliminado'})
    except:
        response = jsonify({"menssage":"Error al Eliminar"})
        response.status = 401
        return response

#controlador actualizar proyecto
def actualizar_proyecto(collections, id):
    try:
        proyecto_data = collections.find_one({'_id': ObjectId(id)})
        proyecto_data_update = ProyectoModel(request.json)

        #insertando datos sencibles
        proyecto_data_update.create_at = proyecto_data['create_at']
        proyecto_data_update.update_at = datetime.now()
        collections.update_one({'_id': ObjectId(id)}, {"$set": proyecto_data_update.__dict__})
        return jsonify({"message": "Proyecto actualizado"})
    except:
        response = jsonify({"menssage":"error de peticion"})
        response.status = 401
        return response