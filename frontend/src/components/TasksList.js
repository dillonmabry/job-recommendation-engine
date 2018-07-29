import React, { Component } from 'react';
import { Container, ListGroup } from 'reactstrap'
import Task from './Task';
import API from '../api/api'

const tasksAPI = new API({ url: process.env.REACT_APP_API_URL, name: 'api/tasks' })

class TasksList extends Component {
	constructor() {
		super();
		this.state = {
			loading: true,
			tasks: []
		}
	}
	componentDidMount() {
		tasksAPI.endpoints.getAll()
			.then((res) => { 
				this.setState({ tasks: res.data, loading: false }) 
			})
			.catch((error) => { return error })
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
		    { this.state.loading ? '' : taskItems }
		    </ListGroup>
		  </Container>
		)
	}
}

export default TasksList;