from flask import Blueprint, request, jsonify
from repositories.user_repository import UserRepository

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/', methods=['GET'])
def get_users():
    users = UserRepository.get_all()
    return jsonify([u.to_dict() for u in users])

@bp.route('/<id>', methods=['GET'])
def get_user(id):
    user = UserRepository.get_by_id(id)
    if not user:
        return jsonify({"error": "User no encontrado"}), 404
    return jsonify(user.to_dict())

@bp.route('/', methods=['POST'])
def create_user():
    data = request.json
    user = UserRepository.create(data)
    return jsonify(user.to_dict()), 201