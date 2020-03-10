from flask import Blueprint, jsonify, request, Response
from Helper.ConvertDict import AlchemyEncoder
from model.Todo import Todo
from app import db
import json


todo_api = Blueprint('todo_api', __name__)


@todo_api.route('/todo', methods=['GET'])
def get_all_todo():
    data = Todo.query.all()
    return json.dumps(data, cls=AlchemyEncoder)


@todo_api.route('/todo', methods=['POST'])
def add_todo():
    data = request.get_json()
    todo = Todo(id=data.get('id'), title=data.get('title'),
                is_completed=data.get('completed'))
    db.session.add(todo)
    db.session.commit()
    return jsonify(data)


@todo_api.route('/todo/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return Response(status=200)


@todo_api.route('/todo/<todo_id>', methods=['PUT'])
def change_todo_state(todo_id):
    print("todo_id: ", todo_id)
    return Response(status=200)
