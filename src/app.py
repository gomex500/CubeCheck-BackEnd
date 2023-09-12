import collections
from datetime import datetime
from http import client
from flask import Flask, request, jsonify
from flask_cors import CORS
from bson import ObjectId
from pymongo import MongoClient
from config import DEBUG, PORT, MONGO_URI

db = ''
collections = ''

#inicializacion
app = Flask(__name__)

#habilitar cors
CORS(app)


try:
    client = MongoClient(MONGO_URI)
    if client.server_info():
        print("conexion exitosa")
        db = client['cubecheck']
        collections = db['usuarios']
    else:
        print("error de conexio")
except Exception as e:
    print("error: ", str(e))

# Routes
@app.route('/')
def index():
    return "hola mundo"

@app.route('/users', methods=['POST'])
def insertarUsuario():
    id = collections.insert_one({
        'nombre': request.json['nombre'],
        'apellido':request.json['apellido'],
        'edad':request.json['edad'],
        'rol':request.json['rol'],
        'telefono':request.json['telefono'],
        'email': request.json['email'],
        'password':request.json['password'],
        'create_at':datetime.now(),
        'update_at':datetime.now()
    })
    return jsonify(str(ObjectId(id)))

@app.route('/users', methods=['GET'])
def getUsuarios():
    users = []
    for doc in collections.find():
        users.append({
            '_id': str(ObjectId(doc['_id'])),
            'nombre': doc['nombre'],
            'apellido': doc['apellido'],
            'edad': doc['edad'],
            'rol': doc['rol'],
            'telefono': doc['telefono'],
            'email': doc['email'],
            'password': doc['password'],
            'create_at': doc['create_at'],
            'update_at': doc['update_at']
        })
    return jsonify(users)

@app.route('/user/<id>', methods=['GET'])
def getUser(id):
  doc = collections.find_one({'_id': ObjectId(id)})
  return jsonify({
            '_id': str(ObjectId(doc['_id'])),
            'nombre': doc['nombre'],
            'apellido': doc['apellido'],
            'edad': doc['edad'],
            'rol': doc['rol'],
            'telefono': doc['telefono'],
            'email': doc['email'],
            'password': doc['password'],
            'create_at': doc['create_at'],
            'update_at': doc['update_at']
        })

@app.route('/user/<id>', methods=['DELETE'])
def eliminarUsuario(id):
  collections.delete_one({'_id': ObjectId(id)})
  return jsonify({'mensaje': 'Usuario eliminado'})

@app.route('/user/<id>', methods=['PUT'])
def updateUser(id):
  collections.update_one({'_id': ObjectId(id)}, {"$set": {
    'nombre': request.json['nombre'],
    'apellido':request.json['apellido'],
    'edad':request.json['edad'],
    'rol':request.json['rol'],
    'telefono':request.json['telefono'],
    'email': request.json['email'],
    'password':request.json['password'],
    'update_at':datetime.now()
  }})
  return jsonify({'message': 'Usuario actualizado'})


if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)