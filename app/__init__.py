#!/usr/bin/python3
"""setup Flask App"""
from flask import Flask
from app.routes import *

def create_app():
    app = Flask(__name__)

    app.register_blueprint(app_bp)

    return app
