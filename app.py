from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory storage for todos
todos = [
    {"id": 1, "task": "Learn Docker", "completed": False},
    {"id": 2, "task": "Set up CI/CD", "completed": False}
]

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Todo API!", "status": "running"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({"todos": todos})

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    new_todo = {
        "id": len(todos) + 1,
        "task": data.get('task'),
        "completed": False
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    for todo in todos:
        if todo['id'] == todo_id:
            todo['completed'] = data.get('completed', todo['completed'])
            todo['task'] = data.get('task', todo['task'])
            return jsonify(todo)
    return jsonify({"error": "Todo not found"}), 404

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return jsonify({"message": "Todo deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)