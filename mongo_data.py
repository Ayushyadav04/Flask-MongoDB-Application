from faker import Faker
from pymongo import MongoClient
#connect to mongodb
client=MongoClient('mongodb://localhost:27017')  # Connection String
database=client['app_data']         # Database name
collection=database['users']        # Collection name
#generate user data
fake=Faker()      #using faker to generate database
users=[]
for i in range(40):
    user={'name':fake.name(),'email':fake.email(),'password':fake.password()}
    users.append(user)
# insert users into mongodb collection
result = collection.insert_many(users)
client.close()
