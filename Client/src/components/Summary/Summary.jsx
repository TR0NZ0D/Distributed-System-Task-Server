import axios from 'axios'
import React, { useState, useEffect } from 'react'
import './style.css';

const Summary = () => {
  const [completedTasksCount, setCompletedTasksCount] = useState(0);
  const [pendingTasksCount, setPendingTasksCount] = useState(0);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setLoading(true)

    axios.get("http://localhost:8000/api/reports/count/")
      .then(response => {
        if (response.status === 200) {
          console.log(response);
          setCompletedTasksCount(response.data.content.completed_count)
          setPendingTasksCount(response.data.content.pending_count)
        }
      })
      .finally(() => {
        setLoading(false);
      })
  }, []);

  return (
    <>
      {loading &&
        <div className="loading">
          <h4>Carregando...</h4>
        </div>}

      {!loading &&
        <div className="summary">
          <div className="summary-square">
            <h4>{completedTasksCount}</h4>
            <h6>Tarefas completadas</h6>
          </div>

          <div className="summary-square">
            <h4>{pendingTasksCount}</h4>
            <h6>Tarefas pendentes</h6>
          </div>

          <div className="summary-square">
            <h4>{completedTasksCount + pendingTasksCount}</h4>
            <h6>Total de tarefas</h6>
          </div>
        </div>}
    </>
  )
}

export default Summary