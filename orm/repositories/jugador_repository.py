from models.jugador import Jugador
from extensions import db
from bson import ObjectId  # <-- importante

class JugadorRepository:

    @staticmethod
    def get_all():
        return Jugador.query.all()

    @staticmethod
    def get_by_id(id):
        return Jugador.query.get(id)

    @staticmethod
    def create(data):
        # Generar _id si no viene
        if "_id" not in data:
            data["_id"] = str(ObjectId())

        jugador = Jugador(**data)
        db.session.add(jugador)
        db.session.commit()
        return jugador

    @staticmethod
    def update(jugador, data):
        for key, value in data.items():
            setattr(jugador, key, value)
        db.session.commit()
        return jugador

    @staticmethod
    def delete(jugador):
        db.session.delete(jugador)
        db.session.commit()