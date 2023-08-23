import React from "react";
import TaskForm from '../../components/TaskForm/TaskForm';
import Navbar from "../../components/Navbar/Navbar";
import { useState } from "react";
import Summary from "../../components/Summary/Summary";

const Home = () => {

  const [active, setActive] = useState("tasks");

  return (
    <>
      <Navbar
        active={active}
        onTasksClick={() => setActive("tasks")}
        onRelatoryClick={() => setActive("relatory")} />

      {active === "tasks" && <TaskForm />}
      {active === "relatory" && <Summary />}
    </>
  )
}

export default Home;
