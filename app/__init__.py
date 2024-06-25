#!/usr/bin/python3
"""setup Flask App"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    """Configure PostgreSQL database"""
    conn = 'postgresql://srecord_user:srecord@localhost/srecord_db'

    # Configuring the Flask application to use a PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = conn

    # Disabling modification tracking to save resources
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['JWT_SECRET_KEY'] = 'c29181e181b7414a9c3c2571be1377ab'
    bcrypt = Bcrypt(app)
    jwt = JWTManager(app)

    CORS(app)

    # Initializing the db object with the Flask app
    db.init_app(app)

    # register blueprint
    app.register_blueprint(app_bp)

    return app



from app.routes import *

