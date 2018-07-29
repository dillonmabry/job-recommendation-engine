import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import PropTypes from 'prop-types';
import { ListGroupItem, Badge, Button } from 'reactstrap'

class Task extends Component {
    constructor(props) {
        super(props);
        this.state = {
            task: props.task
        }  
    }
    render() {
        return (
          <ListGroupItem color="light">
            <p>Task ID: {this.state.task.id}</p>
            <p>Status: <Badge color={this.state.task.done ? 'success' : 'danger'}>
                    {this.state.task.done.toString()}
                </Badge>
            </p>
            <Link to={`/task/${this.state.task.id}`}>
                <Button color="primary">View Details</Button>
            </Link>
          </ListGroupItem>
        )
    }
}
Task.propTypes  = {
    id: PropTypes.number,
    done: PropTypes.bool
}
export default Task;