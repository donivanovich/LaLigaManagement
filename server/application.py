from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt
from pymongo import MongoClient
from bson import ObjectId
import bcrypt, os, urllib.parse, datetime
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

# Mongo
user = os.getenv('MONGO_USER')
passw = os.getenv('MONGO_PASS')
host = os.getenv('MONGO_HOST')
MONGO_URI = f"mongodb+srv://{urllib.parse.quote_plus(user)}:{urllib.parse.quote_plus(passw)}@{host}/pybancodb"
client = MongoClient(MONGO_URI)
db = client.pybancodb
users_col = db.users
pres_col = db.presidentes
jug_col = db.jugadores
pag_col = db.pagos
entrs_col = db.entrenadores

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = users_col.find_one({'email': data['email']})
    if user and bcrypt.checkpw(data['password'].encode(), user['password']):
        token = create_access_token(identity=str(user['_id']))
        return jsonify({'token': token})
    return jsonify({'msg': 'Credenciales inválidas'}), 401

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    
    if not data.get('email') or not data.get('password'):
        return jsonify({'msg': 'Email y contraseña requeridos'}), 400
    
    role = data.get('role', 'user')
    if users_col.find_one({'email': data['email']}):
        return jsonify({'msg': 'Email ya registrado'}), 400
    
    hashed = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
    user_doc = {
        'email': data['email'], 
        'password': hashed,
        'role': role
    }
    user_id = users_col.insert_one(user_doc).inserted_id
    
    return jsonify({
        'msg': 'Usuario creado correctamente', 
        'user_id': str(user_id)
    }), 201


@app.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    users = list(users_col.find({}, {'password': 0}))
    for u in users: u['id'] = str(u.pop('_id'))
    return jsonify(users)

@app.route('/presidentes', methods=['GET'])
@jwt_required()
def get_presidentes():
    pres = list(pres_col.find())
    for p in pres: p['id'] = str(p.pop('_id'))
    return jsonify(pres)

@app.route('/jugadores', methods=['GET'])
@jwt_required()
def get_jugadores():
    jugs = list(jug_col.find())
    for j in jugs:
        j['id'] = str(j.pop('_id'))
        if 'presidente_id' in j:
            j['presidente_id'] = str(j['presidente_id'])
    return jsonify(jugs)

@app.route('/entrenadores', methods=['GET'])
@jwt_required()
def get_entrenadores():
    entrs = list(entrs_col.find())
    for e in entrs:
        e['id'] = str(e.pop('_id'))
        if 'presidente_id' in e:
            e['presidente_id'] = str(e['presidente_id'])
    return jsonify(entrs)

@app.route('/pagos', methods=['GET'])
@jwt_required()
def get_pagos():
    pagos = list(pag_col.find().sort('_id', 1))
    for p in pagos:
        p['id'] = str(p.pop('_id'))
        if 'jugador_id' in p: p['jugador_id'] = str(p['jugador_id'])
        if 'presidente_id' in p: p['presidente_id'] = str(p['presidente_id'])
    return jsonify(pagos)

@app.route('/user/change-password', methods=['PUT'])
@jwt_required()
def change_password():
    user_id = get_jwt()['sub']
    data = request.json
    
    if 'current_password' not in data or 'new_password' not in data:
        return jsonify({'msg': 'Faltan current_password o new_password'}), 400
    
    user = users_col.find_one({'_id': ObjectId(user_id)})
    if not user or not bcrypt.checkpw(data['current_password'].encode(), user['password']):
        return jsonify({'msg': 'Contraseña actual incorrecta'}), 401
    
    hashed = bcrypt.hashpw(data['new_password'].encode(), bcrypt.gensalt())
    users_col.update_one(
        {'_id': ObjectId(user_id)}, 
        {'$set': {'password': hashed}}
    )
    
    return jsonify({'msg': 'Contraseña actualizada correctamente'}), 200

@app.route('/jugadores/<jugador_id>', methods=['DELETE'])
@jwt_required()
def delete_jugador(jugador_id):
    try:
        result = jug_col.delete_one({'_id': ObjectId(jugador_id)})
        if result.deleted_count:
            return jsonify({'msg': 'Jugador eliminado'}), 200
        return jsonify({'msg': 'Jugador no encontrado'}), 404
    except:
        return jsonify({'msg': 'ID inválido'}), 400

@app.route('/presidentes/<presi_id>', methods=['PUT'])
@jwt_required()
def update_presidente(presi_id):
    try:
        data = request.json
        if not data.get('nombre') or 'presupuesto' not in data:
            return jsonify({'msg': 'Faltan nombre o presupuesto'}), 400
        
        result = pres_col.update_one(
            {'_id': ObjectId(presi_id)},
            {'$set': {
                'nombre': data['nombre'],
                'presupuesto': data['presupuesto']
            }}
        )
        
        if result.modified_count:
            return jsonify({'msg': 'Presidente actualizado'}), 200
        return jsonify({'msg': 'No encontrado'}), 404
        
    except Exception as e:
        return jsonify({'msg': 'ID inválido'}), 400

@app.route('/pagos', methods=['POST'])
@jwt_required()
def create_pago():
    data = request.json
    if not all(k in data for k in ['jugador_id', 'presidente_id', 'cantidad', 'estado']):
        return jsonify({'msg': 'Faltan jugador_id, presidente_id, cantidad o estado'}), 400
    
    pago_doc = {
        'jugador_id': ObjectId(data['jugador_id']),
        'presidente_id': ObjectId(data['presidente_id']),
        'cantidad': data['cantidad'],
        'estado': data['estado'],
        'fecha': datetime.datetime.now()
    }
    
    result = pag_col.insert_one(pago_doc)
    return jsonify({'msg': 'Creado', 'pago_id': str(result.inserted_id)}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
