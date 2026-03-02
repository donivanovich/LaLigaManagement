import os
import urllib.parse
from datetime import datetime, timezone
from dataclasses import dataclass
from pymongo import MongoClient
from flask import Flask
from app import create_app
from extensions import db
from repositories.user_repository import UserRepository
from repositories.jugador_repository import JugadorRepository
from repositories.entrenador_repository import EntrenadorRepository
from repositories.presidente_repository import PresidenteRepository
from repositories.pago_repository import PagoRepository
from dotenv import load_dotenv

load_dotenv()

# ------------------------
# Data Classes
# ------------------------
@dataclass
class UserData:
    email: str
    password: str
    role: str

@dataclass
class JugadorData:
    nombre: str
    posicion: str
    sueldo: int
    presidente_id: str

@dataclass
class EntrenadorData:
    nombre: str
    sueldo: int
    presidente_id: str

@dataclass
class PresidenteData:
    nombre: str
    club: str
    presupuesto: int

@dataclass
class PagoData:
    jugador_id: str
    presidente_id: str
    cantidad: float
    estado: str
    fecha: str

# ------------------------
# MongoDB Connection
# ------------------------
user = os.getenv('MONGO_USER')
passw = os.getenv('MONGO_PASS')
host = os.getenv('MONGO_HOST')

mongo_client = MongoClient(f"mongodb+srv://{urllib.parse.quote_plus(user)}:{urllib.parse.quote_plus(passw)}@{host}/pybancodb")
db_mongo = mongo_client.pybancodb

# ------------------------
# App Flask
# ------------------------
app = create_app()

# ------------------------
# Insert Functions
# ------------------------
def insert_user_mongo(data: dict) -> UserData:
    result = db_mongo.users.insert_one(data)
    mongo_user = db_mongo.users.find_one({"_id": result.inserted_id})
    return UserData(email=mongo_user["email"], password=mongo_user["password"], role=mongo_user["role"])

def insert_jugador_mongo(data: dict) -> JugadorData:
    result = db_mongo.jugadores.insert_one(data)
    mongo_j = db_mongo.jugadores.find_one({"_id": result.inserted_id})
    return JugadorData(
        nombre=mongo_j["nombre"],
        posicion=mongo_j["posicion"],
        sueldo=mongo_j["sueldo"],
        presidente_id=mongo_j["presidente_id"]
    )

def insert_entrenador_mongo(data: dict) -> EntrenadorData:
    result = db_mongo.entrenadores.insert_one(data)
    mongo_e = db_mongo.entrenadores.find_one({"_id": result.inserted_id})
    return EntrenadorData(
        nombre=mongo_e["nombre"],
        sueldo=mongo_e["sueldo"],
        presidente_id=mongo_e["presidente_id"]
    )

def insert_presidente_mongo(data: dict) -> PresidenteData:
    result = db_mongo.presidentes.insert_one(data)
    mongo_p = db_mongo.presidentes.find_one({"_id": result.inserted_id})
    return PresidenteData(
        nombre=mongo_p["nombre"],
        club=mongo_p["club"],
        presupuesto=mongo_p["presupuesto"]
    )

def insert_pago_mongo(data: dict) -> PagoData:
    result = db_mongo.pagos.insert_one(data)
    mongo_pago = db_mongo.pagos.find_one({"_id": result.inserted_id})
    return PagoData(
        jugador_id=mongo_pago["jugador_id"],
        presidente_id=mongo_pago["presidente_id"],
        cantidad=mongo_pago["cantidad"],
        estado=mongo_pago["estado"],
        fecha=mongo_pago["fecha"]
    )

# ------------------------
# Add Functions with destino
# ------------------------
def add_user(data: dict, destino="ambos"):
    if destino in ["mongodb", "ambos"]:
        user_dc = insert_user_mongo(data)
        print("User creado en MongoDB:", user_dc)
    if destino in ["mysql", "ambos"]:
        user_mysql = UserRepository.create(data)
        print("User creado en MySQL:", user_mysql.to_dict())

def add_jugador(data: dict, destino="ambos"):
    if destino in ["mongodb", "ambos"]:
        jugador_dc = insert_jugador_mongo(data)
        print("Jugador creado en MongoDB:", jugador_dc)
    if destino in ["mysql", "ambos"]:
        jugador_mysql = JugadorRepository.create(data)
        print("Jugador creado en MySQL:", jugador_mysql.to_dict())

def add_entrenador(data: dict, destino="ambos"):
    if destino in ["mongodb", "ambos"]:
        entrenador_dc = insert_entrenador_mongo(data)
        print("Entrenador creado en MongoDB:", entrenador_dc)
    if destino in ["mysql", "ambos"]:
        entrenador_mysql = EntrenadorRepository.create(data)
        print("Entrenador creado en MySQL:", entrenador_mysql.to_dict())

def add_presidente(data: dict, destino="ambos"):
    if destino in ["mongodb", "ambos"]:
        presidente_dc = insert_presidente_mongo(data)
        print("Presidente creado en MongoDB:", presidente_dc)
    if destino in ["mysql", "ambos"]:
        presidente_mysql = PresidenteRepository.create(data)
        print("Presidente creado en MySQL:", presidente_mysql.to_dict())

def add_pago(data: dict, destino="ambos"):
    if destino in ["mongodb", "ambos"]:
        pago_dc = insert_pago_mongo(data)
        print("Pago creado en MongoDB:", pago_dc)
    if destino in ["mysql", "ambos"]:
        pago_mysql = PagoRepository.create(data)
        print("Pago creado en MySQL:", pago_mysql.to_dict())

# ------------------------
# Main
# ------------------------
def main():
    print("Qué tipo de dato quieres crear?")
    print("1. User\n2. Jugador\n3. Entrenador\n4. Presidente\n5. Pago")
    choice = input("Elige 1-5: ")

    data = {}
    destino = input("Dónde quieres subir los datos? (1=MongoDB, 2=MySQL, 3=Ambos): ")
    dest_map = {"1": "mongodb", "2": "mysql", "3": "ambos"}
    destino = dest_map.get(destino, "ambos")

    if choice == "1":
        data["email"] = input("Email: ")
        data["password"] = input("Password: ")
        data["role"] = input("Role: ")
        add_user(data, destino)
    elif choice == "2":
        data["nombre"] = input("Nombre: ")
        data["posicion"] = input("Posicion: ")
        data["sueldo"] = int(input("Sueldo: "))
        data["presidente_id"] = input("ID Presidente: ")
        add_jugador(data, destino)
    elif choice == "3":
        data["nombre"] = input("Nombre: ")
        data["sueldo"] = int(input("Sueldo: "))
        data["presidente_id"] = input("ID Presidente: ")
        add_entrenador(data, destino)
    elif choice == "4":
        data["nombre"] = input("Nombre: ")
        data["club"] = input("Club: ")
        data["presupuesto"] = float(input("Presupuesto: "))
        add_presidente(data, destino)
    elif choice == "5":
        data["jugador_id"] = input("ID Jugador: ")
        data["presidente_id"] = input("ID Presidente: ")
        data["cantidad"] = float(input("Cantidad: "))
        data["estado"] = input("Estado: ")
        data["fecha"] = datetime.now(timezone.utc).isoformat(timespec='milliseconds')
        add_pago(data, destino)
    else:
        print("Opción inválida")
        return

if __name__ == "__main__":
    with app.app_context():
        main()