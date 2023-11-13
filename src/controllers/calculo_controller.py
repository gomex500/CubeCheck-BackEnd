import math
from flask import request, jsonify
from src.models.materialesY_model import MateYModel
from src.models.materialesX_model import MateXModel
import json

#calcular Pared
def calcular_pared (mateX,mateY):
    try:
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
        data = json.loads(request.data)

        if data['material'] == "Piedra":
            for my in matey:
                if my['tipo'] == "Piedra":
                    print(my)
                    materialBase = my
            print("Piedra")
        elif data['material'] == "Ladrillo":
            for my in matey:
                if my['tipo'] == "Ladrillo":
                    materialBase = my
            print("Ladrillo")
        elif data['material'] == "Bloque":
            for my in matey:
                if my['tipo'] == "Bloque":
                    materialBase = my

        precios = {
            "cemento":0,
            "arena":0
        }

        for mx in matex:
            if mx['tipo'] == "Arena":
                precios['arena'] = mx['precio']
            elif mx['tipo'] == "Cemento":
                precios['cemento'] = mx['precio']

        area = int((data['base']*data['altura'])/(((materialBase['y']+1.5)/100)*((materialBase['z']+1.5)/100)));
        mortero = (data['base'] * data['altura'] * (materialBase['x'] / 100))-(area * (materialBase['z']/100) * (materialBase['y']/100) * (materialBase['x'] / 100));
        cemento = round(float((302 * mortero)*1.05), 2)
        arena = round(float(1.2 * mortero),2)
        agua = round(float(240 * mortero),2)

        res = {
            "Arena": {
                "cantidad":round(arena/0.019,2),
                "precio":round(arena*precios['arena'],2)
            },
            "Agua": agua,
            "Cemento": {
                "cantidad":round(cemento,2),
                "precio":round(cemento*precios['cemento'],2)
            },
            "Ladrillos": {
                "cantidad":round(area,2),
                "precio":round(area*materialBase['precio'],2)
            }
        }
        return res
        # are = int()
    except Exception as e:
        response = jsonify({"message": "Error de petición", "error": str(e)})
        response.status_code = 500
        return response

#calcular pilar
def calcular_pilar (mateX):
    try:
        matex = []
        for doc in mateX.find():
            mate = MateXModel(doc).__dict__
            mate['_id'] = str(doc['_id'])
            matex.append(mate)
            
        data = json.loads(request.data)

        area = data['altura'] * data['ancho'] * data['largo']
        arena = area * 0.52
        cemento = area * 9.73
        grava = area * 0.53
        agua = area * 0.186

        aceroY = 3.6 + (data['altura'] * 4)
        estribo = 0.45 * ((5 + ((data['altura'] * 100) - 25)) / 10)

        precios = {
            "cemento":0,
            "arena":0,
            "grava" : 0,
            "hierroLiso" : 0,
            "hierroCorrugado" : 0
        }

        for mx in matex:
            if mx['tipo'] == "Arena":
                precios['arena'] = mx['precio']
            elif mx['tipo'] == "Cemento":
                precios['cemento'] = mx['precio']
            elif mx['tipo'] == "Hierro":
                precios['hierroLiso'] = mx['precio']
                precios['hierroCorrugado'] = mx['precio']
            elif mx['tipo'] == "Piedrin":
                precios['grava'] = mx['precio']


        res = {
            "arena" : {
                "cantidad" : round(arena/0.019,2),
                "precio" : round(arena * precios['arena'],2)
            },
            "cemento" : {
                "cantidad" : round(cemento,2),
                "precio" : round(cemento * precios['cemento'],2)
            },
            "grava" : {
                "cantidad" : round(grava/0.019,2),
                "precio" : round(grava * precios['grava'],2)
            },
            "hierroCorrugado" : {
                "cantidad" : round(aceroY, 2),
                "precio" : round(aceroY * precios['hierroCorrugado'], 2)
            },
            "hierroLiso" : {
                "cantidad" : round(estribo, 2),
                "precio" : round(estribo * precios['hierroLiso'],2)
            },
            "agua" : int(agua * 1000)
        }

        return res

    except Exception as e:
        response = jsonify({"message": "Error de petición", "error": str(e)})
        response.status_code = 500
        return response

#calcular pilar
def calcular_embaldosado (mateX):
    try:
        matex = []
        for doc in mateX.find():
            mate = MateXModel(doc).__dict__
            mate['_id'] = str(doc['_id'])
            matex.append(mate)
            
        data = json.loads(request.data)

        area = data['largo'] * data['ancho'] * data['grosor']
        arena = area * 0.55
        cemento = area * 350
        grava = area * 0.84
        agua = area * 0.170

        precios = {
            "cemento":0,
            "arena":0,
            "grava" : 0,
        }

        for mx in matex:
            if mx['tipo'] == "Arena":
                precios['arena'] = mx['precio']
            elif mx['tipo'] == "Cemento":
                precios['cemento'] = mx['precio']
            elif mx['tipo'] == "Piedrin":
                precios['grava'] = mx['precio']


        res = {
            "arena" : {
                "cantidad" : round(arena/0.019,2),
                "precio" : round(arena * precios['arena'],2)
            },
            "cemento" : {
                "cantidad" : round(cemento,2),
                "precio" : round(cemento * precios['cemento'],2)
            },
            "grava" : {
                "cantidad" : round(grava/0.019,2),
                "precio" : round(grava * precios['grava'],2)
            },
            "agua" : int(agua * 1000)
        }

        return res

    except Exception as e:
        response = jsonify({"message": "Error de petición", "error": str(e)})
        response.status_code = 500
        return response

