import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Container, Button } from 'reactstrap'
import { Link } from 'react-router-dom';
import API from '../api/api'

const taskAPI = new API({ url: process.env.REACT_APP_API_URL, name: 'api/task' })

class TaskDetail extends Component {
    constructor(props) {
        super(props);
        this.state = {
            details: {
                id: -99,
                done: false
            }
        }
    }
    componentWillMount() {
        taskAPI.endpoints.getOne({ id: this.props.match.params.id })
			.then((res) => { 
                this.setState(prevState => ({
                    details: {
                        ...prevState.details,
                        id: res.data.id,
                        done: res.data.done
                    }
                }))
            })
			.catch((error) => { return error })
    }
    render() {
        return (
          <Container>
            <Link to="/tasks"><Button color="secondary">Back</Button></Link>
            <hr />
            <h2>Task ID: {this.state.details.id}</h2>
            <h2 className="collection-item">Status: {this.state.details.done.toString()}</h2>
          </Container>
        )
    }
}
TaskDetail.propTypes  = {
    id: PropTypes.number,
    done: PropTypes.bool
}
export default TaskDetail;