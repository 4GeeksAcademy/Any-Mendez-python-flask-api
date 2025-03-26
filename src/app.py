from flask import Flask, jsonify
app = Flask(__name__)
from flask import request


todos = [{"label": "My first task", "done": False}]

# @app.route('/myroute', methods=['GET'])
# def hello_world():
#     return 'Hello World!'

# @app.route('/todos', methods=['GET'])
# def hello_world():
#     return "<h1>Hello!</h1>"

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    if 0 <= position < len(todos):
         del todos[position]
         return jsonify(todos)
    else:
        return jsonify({"error": "Position out of range"}), 400    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)