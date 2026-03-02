from flask import Blueprint, request, jsonify
from repositories.presidente_repository import PresidenteRepository

bp = Blueprint('presidentes', __name__, url_prefix='/presidentes')

@bp.route('/', methods=['GET'])
def get_presidentes():
    presidentes = PresidenteRepository.get_all()
    return jsonify([p.to_dict() for p in presidentes])

@bp.route('/<id>', methods=['GET'])
def get_presidente(id):
    presidente = PresidenteRepository.get_by_id(id)
    if not presidente:
        return jsonify({"error": "Presidente no encontrado"}), 404
    return jsonify(presidente.to_dict())

@bp.route('/', methods=['POST'])
def create_presidente():
    data = request.json
    presidente = PresidenteRepository.create(data)
    return jsonify(presidente.to_dict()), 201