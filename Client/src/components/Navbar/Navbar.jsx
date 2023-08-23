import React from 'react';
import './style.css';

const Navbar = ({ active, onTasksClick, onRelatoryClick }) => {

  return (
    <nav className="navbar">
      <span onClick={onTasksClick} className={active === "tasks" ? "active" : ""}>Tarefas</span>
      <span onClick={onRelatoryClick} className={active === "relatory" ? "active" : ""}>Relatorio</span>
    </nav>
  )
}

export default Navbar;