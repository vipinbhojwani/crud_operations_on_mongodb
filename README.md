# Flask-MongoDB CRUD Application
### This is a simple Flask application that demonstrates CRUD operations on a MongoDB database. The application provides a web interface for performing CRUD operations on a collection of documents.

## Requirements
* Python
* Flask
* PyMongo
  
## Installation
* Clone the repository
* Install the required packages: 
  
  `pip install -r requirements.txt`
  
* Start the application: 
  
  `python app.py`
  
* Navigate to http://localhost:5000/ in your web browser to access the application.

## Usage
### The application provides the following endpoints for performing CRUD operations:

* `POST /` - Create a new document
* `GET /` - Display all documents in the collection
* `GET /<id>` - Display a specific document by ID
* `PUT /<id>` - Update a specific document by ID
* `DELETE /<id>` - Delete a specific document by ID

### The application expects JSON data for creating and updating documents. Here's an example of the expected format:

```json
{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "555-555-5555"
}
```

## Configuration
The application expects the following environment variables to be set:

MONGO_URI - The URI of the MongoDB server to connect to (e.g. mongodb://localhost:27017/)
MONGO_DBNAME - The name of the database to use
By default, the application will attempt to connect to a local MongoDB server running on the default port.

License
This application is licensed under the MIT License. See the LICENSE file for details.

Credits
This application was created by [Your Name].