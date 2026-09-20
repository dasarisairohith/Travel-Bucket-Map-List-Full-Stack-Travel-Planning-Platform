from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    jwt.init_app(app)
    CORS(app, origins=[Config.FRONTEND_URL], supports_credentials=True)

    from .routes.auth import auth_bp
    from .routes.destinations import destinations_bp
    from .routes.trips import trips_bp
    from .routes.dashboard import dashboard_bp
    from .routes.places import places_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(destinations_bp, url_prefix="/api/destinations")
    app.register_blueprint(trips_bp, url_prefix="/api/trips")
    app.register_blueprint(dashboard_bp, url_prefix="/api/dashboard")
    app.register_blueprint(places_bp, url_prefix="/api/places")

    with app.app_context():
        from . import models
        db.create_all()

    @app.get("/api/health")
    def health():
        return {"status": "ok"}

    return app
