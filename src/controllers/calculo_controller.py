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
                "cantidad":arena,
                "precio":arena*precios['arena']
            },
            "Agua": agua,
            "Cemento": {
                "cantidad":cemento,
                "precio":cemento*precios['cemento']
            },
            "Ladrillos": {
                "cantidad":area,
                "precio":area*materialBase['precio']
            }
        }
        return res
        # are = int()
    except Exception as e:
        response = jsonify({"message": "Error de petición", "error": str(e)})
        response.status_code = 500
        return response
