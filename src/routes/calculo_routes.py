import imp
from flask import Blueprint, request, jsonify
from src.controllers.jwt import validar_token
from src.configs.conecction import collections
from src.controllers.calculo_controller import (
    calcular_pared,
    calcular_pilar,
    calcular_embaldosado
)

#inicializando rutas de los calculos
calculos_routes = Blueprint('calculos_routes', __name__)

#ruta calcular pared
@calculos_routes.route('/calculoPared', methods=['POST'])
def calcular_pared_ruta():
    return calcular_pared(collections('materiales_x'), collections('materiales_y'))

#ruta calcular pilar
@calculos_routes.route('/calculoPilar', methods=['POST'])
def calcular_pilar_ruta():
    return calcular_pilar(collections('materiales_x'))

#ruta calcular embaldosado
@calculos_routes.route('/calculoEmbaldosado', methods=['POST'])
def calcular_embaldosado_ruta():
    return calcular_embaldosado(collections('materiales_x'))