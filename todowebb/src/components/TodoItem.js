import React from 'react';

const TodoItem = ({ todo, onToggle, onDelete }) => {
  return (
    <div className="todo-item">
      <input
        type="checkbox"
        checked={todo.completed}
        onChange={() => onToggle(todo.id)}
      />
      <div className="todo-text">
        <span className={todo.completed ? 'completed' : ''}>{todo.title}</span>
        {todo.description && <p className="todo-description">{todo.description}</p>}
      </div>
      <button onClick={() => onDelete(todo.id)}>Delete</button>
    </div>
  );
};

export default TodoItem;
