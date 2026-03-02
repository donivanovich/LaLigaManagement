from extensions import db

class User(db.Model):
    __tablename__ = "users"

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(10), nullable=False)

    def to_dict(self):
        return {
            "_id": self._id,
            "email": self.email,
            "role": self.role
        }