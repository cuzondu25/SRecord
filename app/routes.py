#!/usr/bin/python3
from flask import Blueprint

app_bp = Blueprint("app_bp", __name__)

@app_bp.route('/')
def index():
    return "SRecord Api"
