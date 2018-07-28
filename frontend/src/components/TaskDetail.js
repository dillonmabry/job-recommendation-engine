import React, { Component } from 'react';
import { Container, Button } from 'reactstrap'
import { Link } from 'react-router-dom';
import API from '../api/api'

const taskAPI = new API({ url: process.env.REACT_APP_API_URL, name: 'task' })

class TaskDetail extends Component {
    constructor(props) {
        super(props);
        this.state = {
            details: ''
        }
    }
    componentWillMount() {
        taskAPI.endpoints.getOne({ id: this.props.match.params.id })
			.then((res) => { this.setState({ details: res.data }) })
			.catch((error) => { return error })
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