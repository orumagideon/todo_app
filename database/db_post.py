from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from database.models import Todo
from routers.schemas import TodoCreate, TodoUpdate

def create_todo(db: Session, todo: TodoCreate):
    db_todo = Todo(
        title=todo.title,
        description=todo.description,
        completed=todo.completed
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_todos(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieve a list of todos from the database.
    """
    return db.query(Todo).offset(skip).limit(limit).all()

def get_todo_by_id(db: Session, todo_id: int):
    """
    Retrieve a todo by its ID from the database.
    """
    try:
        return db.query(Todo).filter(Todo.id == todo_id).one()
    except NoResultFound:
        return None

def delete_todo_by_id(db: Session, todo_id: int):
    """
    Delete a todo by its ID from the database if it exists.
    """
    todo = get_todo_by_id(db, todo_id)
    if todo is None:
        return None
    db.delete(todo)
    db.commit()
    return todo

def update_todo_by_id(db: Session, todo_id: int, todo_data: TodoUpdate):
    """
    Update an existing todo by its ID.
    """
    todo = get_todo_by_id(db, todo_id)
    if todo is None:
        return None
    
    # Update the fields
    todo.title = todo_data.title
    todo.description = todo_data.description
    todo.completed = todo_data.completed
    
    db.commit()
    db.refresh(todo)
    return todo
