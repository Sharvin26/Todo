from flask import Flask
from flask_cors import CORS, cross_origin
from controller.todos import todos_api

app = Flask(__name__)
CORS(app)
app.register_blueprint(todos_api)
