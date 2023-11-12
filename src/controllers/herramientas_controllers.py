from flask import request, jsonify
from src.models.herramientas_model import HerramientasModel
import json


#controlador insertar herramientas
def insertar_herramienta(collections):
    try:
        data = json.loads(request.data)
        herramienta_instance = HerramientasModel(data)
        id = collections.insert_one(herramienta_instance.__dict__).inserted_id
        return jsonify({'id':str(id)})
    except Exception as e:
        response = jsonify({"message": "Error de petición", "error": str(e)})
        response.status_code = 500
        return response

#controlador herramientas
def obtener_herramientas(collections):
    try:
        tools = []
        for doc in collections.find():
            tool = HerramientasModel(doc).__dict__
            tool['_id'] = str(doc['_id'])
            tools.append(tool)

        return jsonify(tools)
    except Exception as e:
        response = jsonify({"message": "Error de petición", "error": str(e)})
        response.status_code = 500
        return response

#cambiar valor herramienta
def cambiar_valor_herramienta(collections, nombre):
    try:
        print(nombre)
        # Verificar si la herramienta existe
        herramienta_actual = collections.find_one({})
        if not herramienta_actual:
            return jsonify({"message": "La herramienta no existe"}), 404

        # Obtener el valor actual de la herramienta
        valor_actual = herramienta_actual.get(nombre, 0)

        # Actualizar el valor de la herramienta
        nuevo_valor = herramienta_actual.get(nombre, 0) + 1
        collections.update_one({},{"$set": {nombre: nuevo_valor}}
        )

        return jsonify({"message": f"Valor de {nombre} actualizado correctamente"})
    except Exception as e:
        return jsonify({"message": f"Error al actualizar la herramienta: {str(e)}"}), 500