import React, { Component } from 'react';
import { Container } from 'reactstrap'
import Header from '../components/Header'
import API from '../api/api'


const taskAPI = new API({ url: process.env.REACT_APP_FLASK_API_URL, name: 'api/task' })

class TaskDetail extends Component {
    constructor(props) {
        super(props);
        this.state = {
            loading: true,
            details: {
                id: '',
                done: ''
            }
        }
    }
    componentDidMount() {
        taskAPI.endpoints.getOne({ id: this.props.match.params.id })
			.then((res) => { 
                this.setState(prevState => ({
                    details: {
                        ...prevState.details,
                        id: res.data.id,
                        done: res.data.done
                    },
                    loading: false
                }))
            })
			.catch((error) => { console.log(error) })
    }
    render() {
        const taskItem = (
            <div>
                <h2>Task ID: {this.state.details.id}</h2>
                <h2 className="collection-item">
                    Status: {
                        this.state.details.done ? 
                        this.state.details.done.toString() : 
                        'Pending'
                    }
                </h2>
            </div>
        )
        return (
          <Container>
            <Header title={"Task Detail"} back={"tasks"} />
            { this.state.loading ? '' : taskItem }
          </Container>
        )
    }
}
export default TaskDetail;