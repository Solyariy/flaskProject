from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, abort
import work_with_data as dt

app = Flask(__name__, static_folder='../static', template_folder='../templates')
example = [
    {'id': 1, 'name': 'Jack', 'username': 'Obijaka', 'age': 19, 'friends': ['Opaka']}
]

@app.route('/get_users', methods=['GET'])
def get_users():
    return jsonify({'users': dt.get_data()})


@app.route('/get_user/<string:username>', methods=['GET'])
def get_user(username):
    user = dt.find_user(username, dt.get_data())
    if user:
        return jsonify(user)
    abort(404, description="User not found")


@app.route('/create_user', methods=['POST'])
def create_user():
    username = request.json['username']
    users = dt.get_data()
    if dt.find_user(username, users):
        abort(404, description="Username is taken")
    new_user = {
        'name': request.json['name'],
        'username': username,
        'age': request.json['age'],
        'friends': request.json['friends'],
        'password': request.json['password']
    }
    # users.append(new_user)
    dt.push_data(new_user)
    return jsonify(new_user), 201


@app.route('/update_user/<string:username>', methods=['PUT'])
def update_user(username):
    users = dt.get_data()
    user = dt.find_user(username, users)
    print(users, 'users')
    if not user:
        abort(404, description="User not found")

    if not request.json:
        abort(400, description="Invalid request payload")
    if request.json['password'] != user['password']:
        abort(404, description="Invalid password")
    print(user, users)
    user['name'] = request.json.get('name', user['name'])
    user['friends'] = request.json.get('friends', user['friends'])
    user['age'] = request.json.get('age', user['age'])
    print(users, 'users2')
    dt.update_with_new(users)
    return jsonify(user)


# DELETE a product
@app.route('/delete_user/<string:username>', methods=['DELETE'])
def delete_user(username):
    users = dt.get_data()
    print(users, 'deleteusers')
    user = dt.find_user(username, users)
    if not user:
        abort(404, description="User not found")

    users.remove(user)
    dt.update_with_new(users)
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run()
