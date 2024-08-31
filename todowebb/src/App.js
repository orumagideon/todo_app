import React, { useEffect, useState } from 'react';
import TodoItem from './components/TodoItem';
import TodoForm from './components/TodoForm';
import './App.css';

const BASE_URL = 'http://localhost:8000/';

function App() {
  const [todos, setTodos] = useState([]);

  // Fetch todos from the backend
  useEffect(() => {
    fetch(BASE_URL + 'post/todos/')
      .then(response => response.json())
      .then(data => setTodos(data))
      .catch(error => console.error('Error fetching todos:', error));
  }, []);

  // Add a new todo
  const addTodo = (todo) => {
    fetch(BASE_URL + 'post/todos/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(todo),
    })
    .then(response => response.json())
    .then(newTodo => setTodos([...todos, newTodo]))
    .catch(error => console.error('Error adding todo:', error));
  };

  // Toggle the completed state of a todo
  const toggleTodo = (id) => {
    const todo = todos.find(todo => todo.id === id);
    fetch(BASE_URL + `post/todos/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ ...todo, completed: !todo.completed }),
    })
    .then(response => response.json())
    .then(updatedTodo => {
      setTodos(todos.map(todo => todo.id === id ? updatedTodo : todo));
    })
    .catch(error => console.error('Error updating todo:', error));
  };

  // Delete a todo
  const deleteTodo = (id) => {
    fetch(BASE_URL + `post/todos/${id}`, {
      method: 'DELETE',
    })
    .then(() => {
      setTodos(todos.filter(todo => todo.id !== id));
    })
    .catch(error => console.error('Error deleting todo:', error));
  };

  return (
    <div className="App">
      <h1 className="todo-title">TaskMaster</h1>
      <TodoForm onAdd={addTodo} />
      <div className="todo-list">
        {todos.map(todo => (
          <TodoItem
            key={todo.id}
            todo={todo}
            onToggle={toggleTodo}
            onDelete={deleteTodo}
          />
        ))}
      </div>
    </div>
  );
}

export default App;
