from flask import Blueprint, jsonify, request, Response
import uuid

todos_api = Blueprint('todos_api', __name__)

todo_sample_list = []

@todos_api.route('/todo', methods=['GET'])
def get_all_todos():
    return jsonify(todo_sample_list)

@todos_api.route('/todo', methods=['POST'])
def add_todo():
    data = request.get_json()
    data['id'] = uuid.uuid4().fields[0]
    print(data)
    return jsonify(data)

@todos_api.route('/todo/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    return Response(status=200)