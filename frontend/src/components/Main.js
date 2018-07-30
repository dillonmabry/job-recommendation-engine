import React from 'react';
import { Switch, Route } from 'react-router-dom';
import TasksList from '../containers/TasksList';
import TaskDetail from '../containers/TaskDetail'
import Upload from '../containers/Upload'
import Home from '../components/Home'

const Main = () => (
  <main>
    <Switch>
      <Route exact path='/' component={Home} />
      <Route exact path ='/tasks' component={TasksList} />
      <Route exact path ='/task/:id' component={TaskDetail} />
      <Route exact path ='/upload' component={Upload} />
      {/* <Route component={NotFound}/> */}
    </Switch>
  </main>
)

export default Main;