from extensions import db

class Presidente(db.Model):
    __tablename__ = "presidentes"

    _id = db.Column(db.String(24), primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    club = db.Column(db.String(100), nullable=False)
    presupuesto = db.Column(db.Numeric(15,2), nullable=False)

    entrenadores = db.relationship("Entrenador", back_populates="presidente")
    jugadores = db.relationship("Jugador", back_populates="presidente")
    pagos = db.relationship("Pago", back_populates="presidente")

    def to_dict(self):
        return {
            "_id": self._id,
            "nombre": self.nombre,
            "club": self.club,
            "presupuesto": float(self.presupuesto)
        }