from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from database.db_post import create_todo, get_todos, get_todo_by_id, delete_todo_by_id, update_todo_by_id
from routers.schemas import TodoCreate, TodoUpdate, TodoResponse

router = APIRouter(
    prefix="/post",
    tags=["todos"]
)

@router.post("/todos/", response_model=TodoResponse, summary="Create a new todo")
def create_todo_item(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = create_todo(db, todo)
    if db_todo is None:
        raise HTTPException(status_code=400, detail="Error creating todo")
    return db_todo

@router.get("/todos/", response_model=list[TodoResponse], summary="Get all todos")
def read_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    todos = get_todos(db, skip=skip, limit=limit)
    return todos

@router.get("/todos/{todo_id}", response_model=TodoResponse, summary="Get a todo by ID")
def read_todo_by_id(todo_id: int, db: Session = Depends(get_db)):
    todo = get_todo_by_id(db, todo_id=todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail=f"Todo with id {todo_id} not found")
    return todo

@router.delete("/todos/{todo_id}", response_model=TodoResponse, summary="Delete a todo by ID")
def delete_todo_item(todo_id: int, db: Session = Depends(get_db)):
    todo = delete_todo_by_id(db, todo_id=todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail=f"Todo with id {todo_id} not found")
    return todo

@router.put("/todos/{todo_id}", response_model=TodoResponse, summary="Update a todo by ID")
def update_todo_item(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    db_todo = update_todo_by_id(db, todo_id=todo_id, todo_data=todo)
    if db_todo is None:
        raise HTTPException(status_code=404, detail=f"Todo with id {todo_id} not found")
    return db_todo
