import React from 'react';
import { Switch, Route } from 'react-router-dom';
import TasksList from './TasksList';
import TaskDetail from './TaskDetail'
import Upload from './Upload'

const Main = () => (
  <main>
    <Switch>
      <Route exact path ='/tasks' component={TasksList} />
      <Route exact path ='/task/:id' component={TaskDetail} />
      <Route exact path ='/upload' component={Upload} />
    </Switch>
  </main>
)

export default Main;