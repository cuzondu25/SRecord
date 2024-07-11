#!/usr/bin/python3
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from app.routes import app_bp
from . import db

@app_bp.route('/register', methods=['POST'])
def register():
    """ A function to register a new user
    params:
        data(dict): collect url request data
        username(str): user's username
        password(str): user's password
        new_user(obj): User instance for adding using info to the database
    return:
        success msg
    """

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # tests if user already exist
    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "Username already exists"}), 400

    new_user = User(username=username, password_hash=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully"}), 201

@app_bp.route('/login', methods=['POST'])
def login():
    """ A function to grant user access to protected routes
    return:
        access token
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # fetches user data from the database
    user = User.query.filter_by(username=username).first()

    # checks for password match
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"msg": "Invalid username or password"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token)


@app_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return jsonify(logged_in_as=user.username), 200
