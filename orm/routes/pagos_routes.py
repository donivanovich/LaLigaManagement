from flask import Blueprint, request, jsonify
from repositories.pago_repository import PagoRepository

bp = Blueprint('pagos', __name__, url_prefix='/pagos')

@bp.route('/', methods=['GET'])
def get_pagos():
    pagos = PagoRepository.get_all()
    return jsonify([p.to_dict() for p in pagos])

@bp.route('/<id>', methods=['GET'])
def get_pago(id):
    pago = PagoRepository.get_by_id(id)
    if not pago:
        return jsonify({"error": "Pago no encontrado"}), 404
    return jsonify(pago.to_dict())

@bp.route('/', methods=['POST'])
def create_pago():
    data = request.json
    pago = PagoRepository.create(data)
    return jsonify(pago.to_dict()), 201