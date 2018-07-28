import React, { Component } from 'react';
import { Container, ListGroup } from 'reactstrap'
import Task from './Task';
import tasksJson from '../api/tasks'

class TasksList extends Component {
	constructor() {
		super();
		this.state = {
			tasks: []
		}
	}
	componentWillMount() {
		this.getTasks();
	}
	getTasks() {
        this.setState({ tasks: tasksJson })
	}
	render() {
		const taskItems = this.state.tasks.map((task) => 
		{
			return (
			  <Task key={task.id} task={task} />
			)
		})
		return (
		  <Container>
		    <h2>Current Tasks</h2>
		    <ListGroup>
		    {taskItems}
		    </ListGroup>
		  </Container>
		)
	}
}

export default TasksList;