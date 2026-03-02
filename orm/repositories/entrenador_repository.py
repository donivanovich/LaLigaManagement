from models.entrenador import Entrenador
from extensions import db
from bson import ObjectId  # Para generar _id tipo MongoDB

class EntrenadorRepository:

    @staticmethod
    def get_all():
        """Devuelve todos los entrenadores"""
        return Entrenador.query.all()

    @staticmethod
    def get_by_id(entrenador_id):
        """Devuelve un entrenador por su _id"""
        return Entrenador.query.get(entrenador_id)

    @staticmethod
    def create(data):
        """
        Crea un entrenador.
        data debe ser un dict con: nombre, sueldo, presidente_id
        """
        # Generar _id tipo Mongo si no viene
        if "_id" not in data:
            data["_id"] = str(ObjectId())

        entrenador = Entrenador(**data)
        db.session.add(entrenador)
        db.session.commit()
        return entrenador

    @staticmethod
    def update(entrenador, data):
        """
        Actualiza un entrenador existente.
        entrenador: objeto Entrenador
        data: dict con los campos a actualizar
        """
        for key, value in data.items():
            setattr(entrenador, key, value)
        db.session.commit()
        return entrenador

    @staticmethod
    def delete(entrenador):
        """
        Elimina un entrenador de la base de datos.
        """
        db.session.delete(entrenador)
        db.session.commit()