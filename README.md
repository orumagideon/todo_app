# TaskMaster - Todo Application

TaskMaster is a full-stack todo application built with FastAPI for the backend and React for the frontend. It allows users to create, read, update, and delete todo items, providing a clean and user-friendly interface for managing tasks.

## Features

### Backend (FastAPI)

- **Create a Todo**: Add a new todo item to the database.
- **Read Todos**: Retrieve a list of all todos or get a specific todo by ID.
- **Update a Todo**: Modify an existing todo item in the database.
- **Delete a Todo**: Remove a todo item from the database.

### Frontend (React)

- **Interactive UI**: Add, view, update, and delete tasks with an easy-to-use interface.
- **Task Status**: Mark tasks as completed or incomplete.
- **Responsive Design**: The UI adapts to different screen sizes, providing a consistent experience on both desktop and mobile devices.

## Project Structure

TaskMaster/ │ ├── backend/ │ ├── app/ │ │ ├── main.py │ │ ├── routers/ │ │ └── database/ │ └── requirements.txt │ └── frontend/ ├── src/ │ ├── components/ │ │ ├── TodoItem.js │ │ └── TodoForm.js │ ├── App.js │ ├── App.css │ └── index.js └── package.json

## Backend Setup (FastAPI)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/orumagideon/taskmaster.git
   cd taskmaster/backend
   ```

2. Set Up the Virtual Environment
   python -m venv env
   source env/bin/activate # On Windows use `env\Scripts\activate`
3. Install Dependencies
   pip install -r requirements.txt
   Configuration
   The application uses SQLite for database storage. The database file will be created in the project directory (e.g., todo_api.db).
   Usage
4. Start the Application
   uvicorn app.main:app --reload
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
Frontend Setup (React)
Installation
i) Navigate to the Frontend Directory
cd ../frontend
ii) Install Dependencies
iii) npm install

Usage
Start the React Application
\*npm start
The React app will run on http://localhost:3000.
Custom Styling
The application uses Roboto as the primary font.
The UI is styled using App.css. You can further customize the look and feel by modifying this file.
Contributing
To contribute or modify the application:

Fork the repository.
Create a new branch for your changes.
Submit a pull request with a description of your changes.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For questions or feedback, please reach out via orumagideon535@gmail.com.
