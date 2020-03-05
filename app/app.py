from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from controller.todos import todo_api

app.register_blueprint(todo_api)
