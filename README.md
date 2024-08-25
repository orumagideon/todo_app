# Todo API with FastAPI

This is a simple todo application built with FastAPI. It allows users to create, read, update, and delete todo items. The project uses SQLite for data storage and SQLAlchemy for ORM.

## Features

- **Create a Todo**: Add a new todo item.
- **Read Todos**: Retrieve a list of all todos or get a specific todo by ID.
- **Update a Todo**: Modify an existing todo item.
- **Delete a Todo**: Remove a todo item from the database.

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/todo-api.git
cd todo-api
Set Up the Virtual Environment
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install Dependencies
pip install -r requirements.txt
Configuration
The application uses SQLite for database storage. The database file will be created in the project directory (todo_api.db).
Usage
Start the Application
uvicorn main:app --reload
The server will run on http://127.0.0.1:8000.
API Endpoints
Create a Todo

POST /post/todos/
Request Body: TodoCreate
Response: TodoResponse
Get All Todos

GET /post/todos/
Query Parameters: skip (int), limit (int)
Response: List of TodoResponse
Get a Todo by ID

GET /post/todos/{todo_id}
Response: TodoResponse
Update a Todo by ID

PUT /post/todos/{todo_id}
Request Body: TodoUpdate
Response: TodoResponse
Delete a Todo by ID

DELETE /post/todos/{todo_id}
Response: TodoResponse
Models
Todo
id: Integer (Primary Key)
title: String
description: String (Optional)
completed: Boolean
Error Handling
404 Not Found: Returned when a todo item with the specified ID does not exist.
400 Bad Request: Returned for invalid input or errors during todo creation.
Development
To contribute or modify the application:

Fork the repository.
Create a new branch for your changes.
Submit a pull request with a description of your changes.
License
This project is licensed under the MIT License - see the LICENSE file for details.
NOTE: IMPLEMENTATION OF FRONT END WILL BE COMPLETED SOON!!

Contact
For questions or feedback, please reach out orumagideon535@gmail.com
```
