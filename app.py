from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secretkey"

app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'
mongo = PyMongo(app)

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    
    json = request.json
    name = json['name']
    email = json['email']
    password = json['password']

    if name and email and password and request.method == 'POST':
        hashed_password = generate_password_hash(password)
        id = mongo.db.user.insert_one({'name': name, 'email': email, 'password': hashed_password})
        return jsonify({'message': 'User created successfully.'})
    else:
        return not_found()

# Get all users
@app.route('/users', methods=['GET'])
def get_all_users():
    users = mongo.db.user.find()
    resp = dumps(users)
    return resp

# Get a single user
@app.route('/users/<id>')
def get_user_by_id(id):
    user = mongo.db.user.find_one({'_id': ObjectId(id)})
    resp = dumps(user)
    return resp

# Delete a user
@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    user = mongo.db.user.find_one({'_id': ObjectId(id)})
    if user:
        mongo.db.user.delete_one({'_id': ObjectId(id)})
        result = {'message': 'User deleted successfully'}
    else:
        result = {'message': 'User not found'}
    return jsonify(result)

# Update a user
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    _id = id
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['password']
    
    if _name and _email and _password and _id and request.method == 'PUT':
        _hashed_password = generate_password_hash(_password)
        mongo.db.user.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'name': _name, 'email': _email, 'password': _hashed_password}})
        resp = jsonify("User updated successfully.")
        resp.status_code = 200
        return resp
    else:
        result = not_found()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found' + request.url
    }
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True) 