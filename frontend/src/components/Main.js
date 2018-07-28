import React from 'react';
import { Switch, Route } from 'react-router-dom';
import TasksList from './TasksList';
import TaskDetail from './TaskDetail'

const Main = () => (
  <main>
    <Switch>
      <Route exact path ='/tasks' component={TasksList} />
      <Route exact path ='/task/:id' component={TaskDetail} />
    </Switch>
  </main>
)

export default Main;