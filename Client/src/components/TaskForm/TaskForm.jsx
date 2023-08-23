import React, { Component } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import axios from 'axios';
import TaskTable from '../TaskTable/TaskTable';
import './style.css';

class TaskForm extends Component {
  state = {
    tasks: [],
    taskId: 0,
    taskName: '',
    taskDescription: '',
    action: 'Add'
  }

  componentDidMount() {
    this.getTasks();
  }

  getTasks = () => {
    axios.get('http://localhost:5017/api/todo')
      .then(response => {
        if (response.status === 200) {
          let tasks = response.data;
          tasks = tasks.filter(task => {
            return !task.isCompleted
          })

          this.setState({
            ...this.state,
            tasks: tasks
          })
        }
      })
  }

  insertNewTask = () => {
    const newTask = {
      title: this.state.taskName,
      description: this.state.taskDescription
    }

    axios.post('http://localhost:5017/api/todo', JSON.stringify(newTask), {
      data: JSON.stringify(newTask),
      headers: {
        'Content-type': 'application/json'
      },
      method: 'POST'
    })
      .then(response => {
        if (response.status === 201) {
          this.resetTaskValues();
          this.getTasks();
        }
      })
      .catch(error => {
        console.log(error);
      })
  }

  markAsDone = (task) => {
    axios.post(`http://localhost:5017/api/todo/markdone/${task.id}`, {
      method: 'POST'
    })
      .then(response => {
        if (response.status === 200) {
          let tasks = this.state.tasks.filter(t => {
            return t.id !== task.id;
          })

          this.setState({
            ...this.state,
            tasks: tasks,
          })
        }
      })
  }

  editTask = () => {
    const editedTask = {
      id: this.state.taskId,
      title: this.state.taskName,
      description: this.state.taskDescription
    }
    axios.put('http://localhost:5017/api/todo', JSON.stringify(editedTask), {
      headers: {
        'Content-type': 'application/json'
      },
      method: 'PUT'
    })
      .then(response => {
        if (response.status === 200) {
          this.getTasks();
          this.resetTaskValues();
        }
      })
  }

  deleteTask = (taskReceived) => {
    axios.delete(`http://localhost:5017/api/todo/${taskReceived.id}`, {
      method: 'DELETE',
    })
      .then(response => {
        console.log(response);
        if (response.status === 200) {
          let tasks = this.state.tasks.filter(task => {
            return task !== taskReceived;
          })

          this.setState({
            ...this.state,
            tasks: tasks,
          })
        }
      })
      .catch(error => {
        alert(error);
      })
  }

  resetTaskValues = () => {
    this.setState({
      ...this.state,
      taskTitle: "",
      taskDescription: "",
      taskId: 0,
      action: "Add"
    })
  }

  onNameChange = (event) => {
    this.setState({ taskName: event.target.value });
  }

  onDescriptionChange = (event) => {
    this.setState({
      ...this.state,
      taskDescription: event.target.value
    })
  }

  handleSubmit = (event) => {
    event.preventDefault();

    this.setState({
      ...this.state,
      taskName: '',
      taskDescription: ''
    })

    if (this.state.action === 'Add') {
      this.insertNewTask();
    }

    else {
      this.editTask();
    }
  }

  setEditProps = (task) => {
    this.setState({
      ...this.state,
      taskId: task.id,
      taskName: task.title,
      taskDescription: task.description,
      action: 'Edit'
    })
  }

  render() {
    return (
      <div style={{ padding: '7% 4%' }}>
        <Form onSubmit={this.handleSubmit}>
          <Row>
            <Col sm={3} lg={8}>
              <Form.Group>
                <Form.Control
                  value={this.state.taskName}
                  onChange={this.onNameChange}
                  id="task-name"
                  type="text"
                  placeholder="Insira o título da tarefa"
                  required
                />
              </Form.Group>
            </Col>
            <Col sm={2} lg={4}>
              <Button type="submit">
                {this.state.action === "Edit" && <span>Editar</span>}
                {this.state.action === "Add" && <span>Adicionar</span>}</Button>
            </Col>
          </Row>

          <Row>
            <Col lg={8}>
              <Form.Group>
                <Form.Control
                  value={this.state.taskDescription}
                  onChange={this.onDescriptionChange}
                  id="task-description"
                  type="text"
                  placeholder="Descreva a descrição da tarefa"
                  as="textarea"
                  rows={7}
                  required />
              </Form.Group>
            </Col>
          </Row>
        </Form>

        <h2 style={{ marginTop: "3%" }}>Tarefas Ativas</h2>
        <TaskTable
          onEditTask={this.setEditProps}
          onDeleteTask={this.deleteTask}
          onMarkAsDone={this.markAsDone}
          tasks={this.state.tasks} />
      </div>
    )
  }
}

export default TaskForm;
