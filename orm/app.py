from flask import Flask
from config import Config
from extensions import db

# Importar todos los blueprints
from routes.entrenadores_routes import bp as entrenador_bp
from routes.users_routes import bp as users_bp
from routes.jugadores_routes import bp as jugadores_bp
from routes.pagos_routes import bp as pagos_bp
from routes.presidentes_routes import bp as presidentes_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar la base de datos
    db.init_app(app)

    # Registrar todos los blueprints
    app.register_blueprint(entrenador_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(jugadores_bp)
    app.register_blueprint(pagos_bp)
    app.register_blueprint(presidentes_bp)

    # Crear tablas si no existen
    with app.app_context():
        db.create_all()

    return app

# Crear la app
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)