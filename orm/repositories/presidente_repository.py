from models.presidente import Presidente
from extensions import db
import uuid

class PresidenteRepository:

    @staticmethod
    def get_all():
        return Presidente.query.all()

    @staticmethod
    def get_by_id(id):
        return Presidente.query.get(id)

    @staticmethod
    def create(data):
        # Si no viene _id, generamos uno de 24 caracteres (como Mongo ObjectId)
        if "_id" not in data:
            data["_id"] = uuid.uuid4().hex[:24]  # 🔥 SOLO 24 caracteres

        presidente = Presidente(**data)
        db.session.add(presidente)
        db.session.commit()
        return presidente

    @staticmethod
    def update(presidente, data):
        for key, value in data.items():
            setattr(presidente, key, value)
        db.session.commit()
        return presidente

    @staticmethod
    def delete(presidente):
        db.session.delete(presidente)
        db.session.commit()

    @staticmethod
    def get_with_relations(id):
        return Presidente.query.filter_by(_id=id).first()