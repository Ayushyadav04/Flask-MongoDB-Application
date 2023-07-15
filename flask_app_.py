from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson import ObjectId
from flask_restful import Api, Resource

app=Flask(__name__)                                           # Instance of the Flask application
app.config['MONGO_URI']='mongodb://localhost:27017/app_data'  # URI
client=MongoClient('mongodb://localhost:27017/app_data')      # mongoDB URI
database=client['app_data']                                   # Database name
collection=database['users']                                  # Collection name present in the database
mongo=PyMongo(app)                                            # Instance of Pymongo class  
api=Api(app)


        
class UserResource(Resource):
    # Returns a list of all users and specific user
    def get(self,user_id=None):
        if user_id:
            object_id=ObjectId(user_id)      # convert user_id into objectID
            #function to search provided ID if any otherwise display 404 not found error
            user=collection.find_one({'_id': object_id})   
            user['_id']=str(user['_id'])
            return user
        else:
            users=collection.find()
            user_list=[]
            for user in users:
                user['_id']=str(user['_id'])
                user_list.append(user)
            return user_list
    
    
    # Creates a new user with the specified data.
    def post(self):
        new_user=request.get_json()
        result=collection.insert_one(new_user)   # insert_one uses insert new user and get new unique ID
        user_id=collection.find_one({'_id': result.inserted_id})
        return str(user_id), 201   # 201 represent successful insertion

    
    # Updates the user with the specified ID with the new data
    def put(self, user_id):
        object_id=ObjectId(user_id)
        updated_user={
            'name': request.json['name'],'email': request.json['email'],'password': request.json['password']
        }    # dictionary to input updated data
        # Now match the ID provided and using "$ser" update data with method update_one
        result=collection.update_one({'_id': object_id}, {'$set': updated_user})
        if result.modified_count == 0:
            return {'message': 'Same user found or User not found'}, 404
        return {'message': 'User updated'}
    
    # Deletes the user with the specified ID
    def delete(self,user_id):
        object_id=ObjectId(user_id)
        result=collection.delete_one({'_id': object_id})
        if result.deleted_count==0:
            return {'message': 'User not found'}, 404
        return {'message': 'User deleted'}
    
api.add_resource(UserResource, '/collection', '/collection/<string:user_id>')
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(5000),debug=True)
    
