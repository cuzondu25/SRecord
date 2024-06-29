#!/usr/bin/python3
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models import User, Item, Sale, WeeklyRecord
from datetime import datetime, timedelta
from sqlalchemy import func
from app import db

app_bp = Blueprint("app_bp", __name__)

@app_bp.route('/')
def index():
    return "SRecord Api"

@app_bp.route('/api/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name, 'price': item.price} for item in items])

@app_bp.route('/api/sales', methods=['POST'])
@jwt_required()
def submit_sales():
    data = request.get_json()
    user_id = get_jwt_identity()
    item_id = data.get('item_id')
    quantity = data.get('quantity')
    date = data.get('date')

    new_sale = Sale(user_id=user_id, item_id=item_id, quantity=quantity, date=date)
    db.session.add(new_sale)
    db.session.commit()

    return jsonify({"message": "Sales data submitted successfully"}), 201



def get_weekly_records(user_id):
    """ Computes weekly sales record for a user"""
    today = datetime.today()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(days=6)

    weekly_sales = db.session.query(
        func.sum(Sale.quantity * Item.price).label('total_sales')
    ).join(Item).filter(
        Sale.user_id == user_id,
        Sale.date >= week_start.strftime('%Y-%m-%d'),
        Sale.date <= week_end.strftime('%Y-%m-%d')
    ).first()

    return {
        'user_id': user_id,
        'total_sales': weekly_sales.total_sales if weekly_sales.total_sales else 0,
        'week_start': week_start.strftime('%Y-%m-%d'),
        'week_end': week_end.strftime('%Y-%m-%d')
    }


# Add the new API endpoint to retreive weekly record
@app_bp.route('/api/weekly-records', methods=['GET'])
#@jwt_required()
def weekly_records():
    user_id = 1 #get_jwt_identity()
    records = get_weekly_records(user_id)
    return jsonify(records), 200
