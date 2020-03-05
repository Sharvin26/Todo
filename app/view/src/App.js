import React from 'react';
import { 
        BrowserRouter as Router, 
        Route 
      } from 'react-router-dom';
import axios from 'axios';
import Header from './components/layout';
import AddTodo from './components/AddTodo';
import Todos from './components/Todos';
import About from './components/pages/about';

import './App.css';


const requestUrl = "http://localhost:5000/todo"

class App extends React.Component {

  state = {
    todos: []
  }

  // Get all Todos
  componentDidMount() {
    axios.get(requestUrl)
      .then(res => this.setState({ todos: res.data }));
  }

  // Toggle complete
  markComplete = (id) => {
    this.setState({ todos: this.state.todos.map(todo => {
      if(todo.id === id){
        todo.completed = !todo.completed
      }
      return todo;
      })});
  }

  // Delete Todo
  delTodo = (id) => {
    axios.delete(`http://localhost:5000/todo/${id}`)
      .then(res => this.setState({
        todos: [...this.state.todos.filter(todo =>
          todo.id !== id)]
      }));
  }

  // Add Todo
  addTodo = (title) => {
    axios.post(requestUrl, {
      title,
      completed:false
    }).then(res => this.setState({ 
        todos: [...this.state.todos, res.data] }) );
  }

  render() {
    return (
      <Router>
        <div className="App">
          <div className="container">
            < Header />
            < Route exact path="/" render={props => {
              return (
                <React.Fragment>
                  < AddTodo addTodo={this.addTodo} />
                  < Todos todos={this.state.todos}
                    markComplete={this.markComplete}
                    delTodo={this.delTodo} /> 
                </React.Fragment>
              );
            }} />
            < Route path="/about" component={About} />
          </div>
        </div>
      </Router>
    );
  }
}

export default App;