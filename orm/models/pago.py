from extensions import db
from datetime import datetime

class Pago(db.Model):
    __tablename__ = "pagos"

    _id = db.Column(db.String(24), primary_key=True)
    jugador_id = db.Column(db.String(24), db.ForeignKey("jugadores._id"), nullable=False)
    presidente_id = db.Column(db.String(24), db.ForeignKey("presidentes._id"), nullable=False)
    cantidad = db.Column(db.Numeric(15,2), nullable=False)
    estado = db.Column(db.String(50), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

    jugador = db.relationship("Jugador", back_populates="pagos")
    presidente = db.relationship("Presidente", back_populates="pagos")

    def to_dict(self):
        return {
            "_id": self._id,
            "jugador_id": self.jugador_id,
            "presidente_id": self.presidente_id,
            "cantidad": float(self.cantidad),
            "estado": self.estado,
            "fecha": self.fecha
        }