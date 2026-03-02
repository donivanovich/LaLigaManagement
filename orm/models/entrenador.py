from extensions import db

class Entrenador(db.Model):
    __tablename__ = "entrenadores"

    _id = db.Column(db.String(24), primary_key=True)  # ID tipo Mongo
    nombre = db.Column(db.String(150), nullable=False)
    sueldo = db.Column(db.Integer, nullable=False)
    presidente_id = db.Column(db.String(24), db.ForeignKey("presidentes._id"), nullable=False)

    # Esta es la línea que faltaba
    presidente = db.relationship("Presidente", back_populates="entrenadores")

    def __repr__(self):
        return f"<Entrenador(nombre={self.nombre}, sueldo={self.sueldo}, presidente_id={self.presidente_id})>"

    def to_dict(self):
        return {
            "_id": self._id,
            "nombre": self.nombre,
            "sueldo": self.sueldo,
            "presidente_id": self.presidente_id
        }