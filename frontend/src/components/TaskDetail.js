import React, { Component } from 'react';
// import axios from 'axios';
import { Container, Button } from 'reactstrap'
import { Link } from 'react-router-dom';
import tasks from '../api/tasks'

class TaskDetail extends Component {
    
    constructor(props) {
        super(props);
        this.state = {
            details: ''
        }
    }
    componentWillMount() {
        this.setState({ details: this.getMeetup() })
    }
    getMeetup() {
         let taskId = this.props.match.params.id;
        // axios.get(`/api/tasks/${taskId}`)
		// .then(response => {
		// 	this.setState({details: response.data}, () =>
		// 	{

		// 	});
		// })
        // .catch(err => console.log(err));
        // eslint-disable-next-line
        return tasks.find(task => task.id == taskId);
    }
    render() {
        return (
          <Container>
            <Link to="/"><Button color="secondary">Back</Button></Link>
            <hr />
            <h2>Task ID: {this.state.details.id}</h2>
            <h2 className="collection-item">Status: {this.state.details.ready.toString()}</h2>
          </Container>
        )
    }
}

export default TaskDetail;