import React, { Component } from 'react';
import { Container, ListGroup } from 'reactstrap'
import Task from './Task';
import Header from '../components/Header'
import API from '../api/api'

const tasksAPI = new API({ url: process.env.REACT_APP_FLASK_API_URL, name: 'api/tasks' })

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
			.catch((error) => { console.log(error) })
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
		     <Header title={"Current Tasks"} back={""} />
		    <ListGroup>
		    { this.state.loading ? '' : taskItems }
		    </ListGroup>
		  </Container>
		)
	}
}

export default TasksList;
