from models.user import User
from extensions import db
from bson import ObjectId  # Para generar ObjectId como en MongoDB

class UserRepository:

    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def create(data):
        # Generar _id si no viene
        if "_id" not in data:
            data["_id"] = str(ObjectId())

        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def update(user, data):
        for key, value in data.items():
            setattr(user, key, value)
        db.session.commit()
        return user

    @staticmethod
    def delete(user):
        db.session.delete(user)
        db.session.commit()