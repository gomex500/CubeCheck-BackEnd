from datetime import datetime
from flask import request, jsonify
from bson import ObjectId
from src.models.materialesY_model import MateYModel
from src.models.materialesX_model import MateXModel
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
def obtener_proyectos(collections, user):
    try:
        proyectos = []
        for doc in collections.find({"user": user}):
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
def actualizar_proyecto(collections,mateX, mateY, id):
    try:

        proyecto_data = collections.find_one({'_id': ObjectId(id)})
        # proyecto_data_update = ProyectoModel(request.json)
        contruccion = json.loads(request.data)
        grosorPilarTotal = contruccion["numeroPilares"] * 0.25

        matey = []
        for doc in mateY.find():
            mate = MateYModel(doc).__dict__
            mate['_id'] = str(doc['_id'])
            matey.append(mate)
        
        matex = []
        for doc in mateX.find():
            mate = MateXModel(doc).__dict__
            mate['_id'] = str(doc['_id'])
            matex.append(mate)

        materialBase = {}

        if contruccion["materialBase"] == "Piedra":
            for my in matey:
                if my['tipo'] == "Piedra":
                    materialBase = my
        elif contruccion["materialBase"] == "Ladrillo":
            for my in matey:
                if my['tipo'] == "Ladrillo":
                    materialBase = my
        elif contruccion["materialBase"] == "Bloque":
            for my in matey:
                if my['tipo'] == "Bloque":
                    materialBase = my

        preciosPared = {
            "cemento":0,
            "arena":0
        }

        for mx in matex:
            if mx['tipo'] == "Arena":
                preciosPared['arena'] = mx['precio']
            elif mx['tipo'] == "Cemento":
                preciosPared['cemento'] = mx['precio']

                # nVentanasF = 0;
                # nVentanasT = 0;
                # nVentanasD = 0;
                # nVentanasI = 0;

        # if not contruccion["numeroPilares"]:
        #     if contruccion["numeroPilares"]>4:
        #         nVentanasF = len(contruccion['pilaresZ']);
        #         nVentanasT = len(contruccion['pilaresZN'])+1;
        #         nVentanasD = len(contruccion['pilaresX'])+1;
        #         nVentanasI = len(contruccion['pilaresXN'])+1;
        #         if contruccion["ventanasF"]:
        #             area1+= (1* nVentanasF) * 0.8

        #         if contruccion["ventanasT"]:
        #             area1 = area ((1* nVentanasT) * 0.8)

        #         if contruccion["ventanasD"]:
        #             area1 = area + ((1* nVentanasD) * 0.8)

        #         if contruccion["ventanasI"]:
        #             area1 += (1* nVentanasI) * 0.8
        #     else:
        #         nVentanasF = 1;
        #         nVentanasT = 1;
        #         nVentanasD = 1;
        #         nVentanasI = 1;

        # area1 = 0

        # print(area1);

        #pared
        largoPared = ((contruccion["embaldosado"][0]*2)+(contruccion["embaldosado"][2]*2)) - grosorPilarTotal
        altoPared = contruccion["alturaParedes"]

        area = int((largoPared*altoPared)/(((materialBase['y']+1.5)/100)*((materialBase['z']+1.5)/100)));
        mortero = (largoPared* altoPared * (materialBase['x'] / 100))-(area * (materialBase['z']/100) * (materialBase['y']/100) * (materialBase['x'] / 100));
        cemento = round(float((302 * mortero)*1.05), 2)
        arena = round(float(1.2 * mortero),2)
        agua = round(float(240 * mortero),2)

        resPared = {
            "arena": {
                "cantidad":round(arena/0.019,2),
                "precio":round(arena*preciosPared['arena'],2)
            },
            "agua": agua,
            "Cemento": {
                "cantidad":round(cemento/42.5,2),
                "precio":round(cemento*preciosPared['cemento'],2)
            },
            "ladrillos": {
                "cantidad":round(area,2),
                "precio":round(area*materialBase['precio'],2)
            }
        }

        #pilar
        alturapilar = contruccion["alturaPilares"] * contruccion["numeroPilares"]

        area = alturapilar * 0.25 * 0.25
        arena = area * 0.52
        cemento = area * 9.73
        grava = area * 0.53
        agua = area * 0.186

        aceroY = 3.6 + (alturapilar * 4)
        estribo = 0.45 * ((5 + ((alturapilar * 100) - 25)) / 10)

        preciosPilares = {
            "cemento":0,
            "arena":0,
            "grava" : 0,
            "hierroLiso" : 0,
            "hierroCorrugado" : 0
        }

        for mx in matex:
            if mx['tipo'] == "Arena":
                preciosPilares['arena'] = mx['precio']
            elif mx['tipo'] == "Cemento":
                preciosPilares['cemento'] = mx['precio']
            elif mx['tipo'] == "Hierro":
                preciosPilares['hierroLiso'] = mx['precio']
                preciosPilares['hierroCorrugado'] = mx['precio']
            elif mx['tipo'] == "Piedrin":
                preciosPilares['grava'] = mx['precio']


        resPilares = {
            "arena" : {
                "cantidad" : round(arena/0.019,2),
                "precio" : round(arena * preciosPilares['arena'],2)
            },
            "cemento" : {
                "cantidad" : round(cemento,2),
                "precio" : round((cemento*50) * preciosPilares['cemento'],2)
            },
            "grava" : {
                "cantidad" : round(grava/0.019,2),
                "precio" : round(grava * preciosPilares['grava'],2)
            },
            "hierroCorrugado" : {
                "cantidad" : round(aceroY, 2),
                "precio" : round(aceroY * preciosPilares['hierroCorrugado'], 2)
            },
            "hierroLiso" : {
                "cantidad" : round(estribo, 2),
                "precio" : round(estribo * preciosPilares['hierroLiso'],2)
            },
            "agua" : int(agua * 1000)
        }

        #embaldosado
        area = contruccion["embaldosado"][0] * contruccion["embaldosado"][2] * contruccion["embaldosado"][1]
        arena = area * 0.55
        cemento = area * 350
        grava = area * 0.84
        agua = area * 0.170

        preciosEmbaldosado = {
            "cemento":0,
            "arena":0,
            "grava" : 0,
        }

        for mx in matex:
            if mx['tipo'] == "Arena":
                preciosEmbaldosado['arena'] = mx['precio']
            elif mx['tipo'] == "Cemento":
                preciosEmbaldosado['cemento'] = mx['precio']
            elif mx['tipo'] == "Piedrin":
                preciosEmbaldosado['grava'] = mx['precio']


        resEmbaldosado = {
            "arena" : {
                "cantidad" : round(arena/0.019,2),
                "precio" : round(arena * preciosEmbaldosado['arena'],2)
            },
            "cemento" : {
                "cantidad" : round(cemento/42.5,2),
                "precio" : round(cemento * preciosEmbaldosado['cemento'],2)
            },
            "grava" : {
                "cantidad" : round(grava/0.019,2),
                "precio" : round(grava * preciosEmbaldosado['grava'],2)
            },
            "agua" : int(agua * 1000)
        }

        print(largoPared, altoPared, grosorPilarTotal)

        presupuesto = {
            "cantidadParedes":contruccion["numeroParedes"],
            "presupuestoParedes":resPared,
            "cantidadPilares":contruccion["numeroPilares"],
            "presupuestoPilares":resPilares,
            "presupuestoEmbaldosado":resEmbaldosado
        }
        # Actualizar los campos necesarios con los datos del JSON
        proyecto_data['presupuesto'] = presupuesto
        proyecto_data['construccion'] = contruccion
        
        # Actualizar las fechas
        proyecto_data['update_at'] = datetime.now()

        # Realizar la actualización en la base de datos
        collections.update_one({'_id': ObjectId(id)}, {"$set": proyecto_data})
        return jsonify({"presupuesto":"presupuesto"})
    except Exception as e:
        response = jsonify({"menssage":"error de peticion","erro":str(e)})
        response.status = 401
        return response