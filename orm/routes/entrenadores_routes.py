from flask import Blueprint, request, jsonify
from repositories.entrenador_repository import EntrenadorRepository

bp = Blueprint('entrenadores', __name__, url_prefix='/entrenadores')

@bp.route('/', methods=['GET'])
def get_entrenadores():
    entrenadores = EntrenadorRepository.get_all()
    return jsonify([e.to_dict() for e in entrenadores])

@bp.route('/<id>', methods=['GET'])
def get_entrenador(id):
    entrenador = EntrenadorRepository.get_by_id(id)
    if not entrenador:
        return jsonify({"error": "Entrenador no encontrado"}), 404
    return jsonify(entrenador.to_dict())

@bp.route('/', methods=['POST'])
def create_entrenador():
    data = request.json
    entrenador = EntrenadorRepository.create(data)
    return jsonify(entrenador.to_dict()), 201