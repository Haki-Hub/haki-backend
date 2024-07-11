from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://haki_user:Hakihubke22!@localhost/haki_hub'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Import models to ensure they are registered properly
    from app.models import Category, Bill, Part, Section, Chapter
    with app.app_context():
        db.create_all()
    
    # Register Blueprints
    from .routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
