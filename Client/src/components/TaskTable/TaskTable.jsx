import React from 'react';
import Table from 'react-bootstrap/Table';
import './style.css';

const TaskTable = ({
  tasks,
  onDeleteTask,
  onEditTask,
  onMarkAsDone }) => {
  return (
    <Table striped bordered hover className="to-do-table">
      <thead className="table-head">
        <tr>
          <th>Titulo da tarefa</th>
          <th>Data de criação</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        {
          tasks.map(task => {
            return (
              <tr key={task.id}>
                <td>{task.title}</td>
                <td>{task.createdAt}</td>
                <td>
                  <span onClick={() => onMarkAsDone(task)} className="link-actions">Marcar como concluido</span> |
                  <span onClick={() => onEditTask(task)} className="link-actions">Visualizar</span> |
                  <span onClick={() => onDeleteTask(task)} className="link-actions">Deletar</span>
                </td>
              </tr>
            )
          })
        }
      </tbody>
    </Table>
  )
}

export default TaskTable;
