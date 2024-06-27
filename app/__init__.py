import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Load environment variables from .env file
    load_dotenv()

    # Configure individual settings from .env
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    # Set security headers using after request decorators (optional)
    # You can disable the block of code below if you web app is not using https
    @app.after_request
    def set_security_headers(response):
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        response.headers['X-Content-Type-Options'] = 'nosniff'
        return response

    db.init_app(app)
    migrate.init_app(app, db)

    # Importing models after initializing db
    from app.models import Category, Post, Resource

    # Create tables if they do not exist
    with app.app_context():
        db.create_all()

    # Importing routes and registering blueprints
    from app.routes import main, wagtail
    app.register_blueprint(main.bp)
    app.register_blueprint(wagtail.bp, url_prefix='/wagtail')

    return app
