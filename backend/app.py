from flask import Flask, request, jsonify
from flask_restplus import Api, Resource, fields
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
api = Api(app, version='1.0', title='User API', description='A simple User API')

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

user_model = api.model('User', {
    'name': fields.String(required=True, description='The user name'),
    'email': fields.String(required=True, description='The user email'),
    'age': fields.Integer(required=True, description='The user age'),
    'color': fields.String(required=True, description='The user favorite color'),
})

ns = api.namespace('users', description='User operations')

@ns.route('/')
class UserList(Resource):
    '''Shows a list of all users, and lets you POST to add new users'''
    @ns.doc('list_users')
    @ns.marshal_list_with(user_model)
    def get(self):
        '''Fetch all users'''
        users = mongo.db.users.find()
        return list(users), 200

    @ns.doc('create_user')
    @ns.expect(user_model)
    @ns.marshal_with(user_model, code=201)
    def post(self):
        '''Create a new user'''
        data = request.get_json()
        inserted_user = mongo.db.users.insert_one(data)
        user_id = inserted_user.inserted_id
        user = mongo.db.users.find_one({"_id": user_id})
        return user, 201

@ns.route('/<id>')
@api.response(404, 'User not found')
@api.param('id', 'The user identifier')
class User(Resource):
    '''Show a single user item and lets you delete them'''
    @ns.doc('get_user')
    @ns.marshal_with(user_model)
    def get(self, id):
        '''Fetch a given resource'''
        user = mongo.db.users.find_one({"_id": ObjectId(id)})
        return user, 200

    @ns.doc('delete_user')
    @ns.response(204, 'User deleted')
    def delete(self, id):
        '''Delete a user given its identifier'''
        mongo.db.users.delete_one({"_id": ObjectId(id)})
        return '', 204

    @ns.expect(user_model)
    @ns.marshal_with(user_model)
    def put(self, id):
        '''Update a user given its identifier'''
        data = request.get_json()
        mongo.db.users.update_one({"_id": ObjectId(id)}, {"$set": data})
        user = mongo.db.users.find_one({"_id": ObjectId(id)})
        return user, 200

if __name__ == "__main__":
    app.run(debug=True)
