#!/usr/bin/python3
"""Run app module application"""
from app import create_app, db
from app.models import User, Item, Sale, WeeklyRecord
from app.login_routes import *
from flask_cors import CORS

app = create_app()
CORS(app)

print(app.url_map)

# Creating an application context to work with the app
with app.app_context():
    """ Within this context, Flask knows which app instance to use
        Creating all database tables defined in the SQLAlchemy models
    """
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, threaded=True)


