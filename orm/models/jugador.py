from extensions import db

class Jugador(db.Model):
    __tablename__ = "jugadores"

    _id = db.Column(db.String(24), primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    posicion = db.Column(db.String(50), nullable=False)
    sueldo = db.Column(db.Integer, nullable=False)
    presidente_id = db.Column(db.String(24), db.ForeignKey("presidentes._id"), nullable=False)

    presidente = db.relationship("Presidente", back_populates="jugadores")
    pagos = db.relationship("Pago", back_populates="jugador")

    def to_dict(self):
        return {
            "_id": self._id,
            "nombre": self.nombre,
            "posicion": self.posicion,
            "sueldo": self.sueldo,
            "presidente_id": self.presidente_id
        }