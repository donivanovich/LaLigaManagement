from models.pago import Pago
from extensions import db
import uuid

class PagoRepository:

    @staticmethod
    def get_all():
        return Pago.query.all()

    @staticmethod
    def get_by_id(id):
        return Pago.query.get(id)

    @staticmethod
    def get_by_jugador(jugador_id):
        return Pago.query.filter_by(jugador_id=jugador_id).all()

    @staticmethod
    def get_by_presidente(presidente_id):
        return Pago.query.filter_by(presidente_id=presidente_id).all()

    @staticmethod
    def create(data):
        # Generamos un _id si no viene en los datos
        if "_id" not in data:
            data["_id"] = uuid.uuid4().hex[:24]

        pago = Pago(**data)
        db.session.add(pago)
        db.session.commit()
        return pago

    @staticmethod
    def update(pago, data):
        for key, value in data.items():
            setattr(pago, key, value)
        db.session.commit()
        return pago

    @staticmethod
    def delete(pago):
        db.session.delete(pago)
        db.session.commit()