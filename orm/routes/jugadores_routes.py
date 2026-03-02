from flask import Blueprint, request, jsonify
from repositories.jugador_repository import JugadorRepository

bp = Blueprint('jugadores', __name__, url_prefix='/jugadores')

@bp.route('/', methods=['GET'])
def get_jugadores():
    jugadores = JugadorRepository.get_all()
    return jsonify([j.to_dict() for j in jugadores])

@bp.route('/<id>', methods=['GET'])
def get_jugador(id):
    jugador = JugadorRepository.get_by_id(id)
    if not jugador:
        return jsonify({"error": "Jugador no encontrado"}), 404
    return jsonify(jugador.to_dict())

@bp.route('/', methods=['POST'])
def create_jugador():
    data = request.json
    jugador = JugadorRepository.create(data)
    return jsonify(jugador.to_dict()), 201