import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, DB_NAME)
        print(app.config['SQLALCHEMY_DATABASE_URI'])
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        db.init_app(app)

        from .view1 import view1

        app.register_blueprint(view1, url_prefix = '/')

        from .models import Student

        with app.app_context():
                db.create_all()

        return app

# def create_db(app):
#         if not path.exists("backend/"+DB_NAME):
                
#                 print("Database Created.")
#         else:
#                 print("Database already present.")

# ## Importing Routes
# from backend import view1, view2

# ## Importing DB
# if not path.exists("backend/database.db"):
#         # db.create_all()
#         print("Database Created.")
# else:
#         print("Database already present.")
# db = SQLAlchemy()
# if not path.exists("backend/database.db"):
#         # db.create_all()
#         print("Database Created.")
# else:
#         print("Database already present.")
# db.init_app(app)
# if not path.exists("backend/database.db"):
#         # db.create_all()
#         print("Database Created.")
# else:
#         print("Database already present.")

# from .model import Student
# if not path.exists("backend/database.db"):
#         # db.create_all()
#         print("Database Created.")
# else:
#         print("Database already present.")
# # with app.app_context():
# with app.app_context():
#         if not path.exists("backend/database.db"):
#                 db.create_all()
#                 print("Database Created.")
#         else:
#                 print("Database already present.")

