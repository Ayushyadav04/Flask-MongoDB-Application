# Flask CRUD Application with MongoDB
**This is a Flask application that provides a REST API for performing CRUD operations on a User resource using MongoDB as the database. 
It uses the `faker` library to generate sample user data for testing purposes.**

## Requirements

- Python 
- Flask
- PyMongo
- Faker
- Postman (for testing the REST API endpoints)
- MongoDB (MongoDB server installed and running)

## Steps to be followed to run the application:
1. Clone the repository
2. Create a virtual environment
3. Activate the virtual environment
4. Install the required packages
5. First open `mongo_data.py` in a code editor.
   > Set your own MongoDB URI
   > Set the Database and Collection name
6. Now the Databse has been created and stored in provided MongoDB Collection
7. Now open `flask_app_.py` in code editor.
   > Set your own MongoDB URI
   > Set the Database and Collection name
8. Run the application


## Usage

- The application provides the following REST API endpoints:
- `GET /collection`: Returns a list of all users.
- `GET /collection/<id>`: Returns the user with the specified ID.
- `POST /collection`: Creates a new user with the specified data.
- `PUT /collection/<id>`: Updates the user with the specified ID with the new data.
- `DELETE /collection/<id>`: Deletes the user with the specified ID.

## Testing 
### Use tool Postman to send HTTP requests to the above endpoints and test the CRUD operations on the User resource.
- To read all data
   ![image](https://github.com/Ayushyadav04/Flask-MongoDB-Application/assets/113254994/1027d6de-6421-4c66-8846-116371b71388)

-  To create data
   ![image](https://github.com/Ayushyadav04/Flask-MongoDB-Application/assets/113254994/7783c74d-2f85-41df-8819-3e393c4b13cd)

-  To update data
   ![image](https://github.com/Ayushyadav04/Flask-MongoDB-Application/assets/113254994/6bc6f30b-d25e-4011-a74f-c6980e26b133)

-  To Delete data
   ![image](https://github.com/Ayushyadav04/Flask-MongoDB-Application/assets/113254994/3a422d83-8709-4a81-b35d-0468e5a371fe)



