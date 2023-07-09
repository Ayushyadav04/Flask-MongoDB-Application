from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson import ObjectId
from pymongo import MongoClient


app=Flask(__name__)                                           # Instance of the Flask application
client=MongoClient('mongodb://localhost:27017/app_data')      # mongoDB URI
database=client['app_data']                                   # Database name
collection=database['users']                                  # Collection name present in the database


# Returns a list of all users.
@app.route('/collection', methods=['GET'])              # "users" collection from database app_data
def get_users():
    users=collection.find()  # method find to collect all the data
    user_list=[]
    for i in users:
        i['_id']=str(i['_id'])       # Convert objectID to string rep.
        user_list.append(i)
    return jsonify(user_list)


# Returns the user with the specified ID.
@app.route('/collection/<user_id>', methods=['GET'])
def get_user(user_id):
    object_id=ObjectId(user_id)      # convert user_id into objectID
    #function to search provided ID if any otherwise display 404 not found error
    user=collection.find_one({'_id': object_id})   
    if user:
        user['_id']=str(user['_id'])
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'}), 404


# Creates a new user with the specified data.
@app.route('/collection', methods=['POST'])
def create_user():
    new_user={
        'name': request.json['name'],'email': request.json['email'],'password': request.json['password']
    }   # dictioanry represent new user data
    user_id=collection.insert_one(new_user).inserted_id   # insert_one uses insert new user and get new unique ID
    return jsonify(str(user_id)), 201   # 201 represent successful insertion


# Updates the user with the specified ID with the new data
@app.route('/collection/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    object_id=ObjectId(user_id)
    updated_user={
        'name': request.json['name'],'email': request.json['email'],'password': request.json['password']
    }    # dictionary to input updated data
    # Now match the ID provided and using "$ser" update data with method update_one
    result=collection.update_one({'_id': object_id}, {'$set': updated_user})
    if result.modified_count==0:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'message': 'User updated'})


# Deletes the user with the specified ID
@app.route('/collection/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    object_id=ObjectId(user_id)
    result=collection.delete_one({'_id': object_id})
    if result.deleted_count==0:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'message': 'User deleted'})

if __name__ == '__main__':
    app.run(debug=True)
