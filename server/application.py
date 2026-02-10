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

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = users_col.find_one({'email': data['email']})
    if user and bcrypt.checkpw(data['password'].encode(), user['password']):
        token = create_access_token(identity=str(user['_id']))  # FIX: string simple
        return jsonify({'token': token})
    return jsonify({'msg': 'Credenciales inválidas'}), 401

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if users_col.find_one({'email': data['email']}):
        return jsonify({'msg': 'Email existe'}), 400
    hashed = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
    user_id = users_col.insert_one({
        'email': data['email'], 'password': hashed, 'role': 'user'
    }).inserted_id
    pres_id = pres_col.insert_one({
        'user_id': user_id, 'nombre': data['nombre'], 
        'club': data['club'], 'presupuesto': 500000000
    }).inserted_id
    return jsonify({'msg': 'Registrado', 'pres_id': str(pres_id)}), 201

@app.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    users = list(users_col.find({}, {'password': 0}))
    for u in users: u['id'] = str(u.pop('_id'))
    return jsonify(users)

@app.route('/presidentes', methods=['GET'])
@jwt_required()
def get_presidentes():
    pres = list(pres_col.find({}, {'user_id': 0}))  # Todos
    for p in pres: p['id'] = str(p.pop('_id'))
    return jsonify(pres)

@app.route('/jugadores', methods=['GET'])
@jwt_required()
def get_jugadores():
    jugs = list(jug_col.find({}, {'presidente_id': 0}))  # Todos
    for j in jugs: j['id'] = str(j.pop('_id'))
    return jsonify(jugs)

@app.route('/pagos', methods=['GET'])
@jwt_required()
def get_pagos():
    pagos = list(pag_col.find().sort('_id', 1))
    for p in pagos:
        p['id'] = str(p.pop('_id'))
        if 'jugador_id' in p: p['jugador_id'] = str(p['jugador_id'])
        if 'presidente_id' in p: p['presidente_id'] = str(p['presidente_id'])
    return jsonify(pagos)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
