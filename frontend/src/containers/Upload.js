import React, { Component } from 'react';
import { 
    Container, 
    Form, 
    FormGroup, 
    Label, 
    Input, 
    ListGroup, 
    ListGroupItem,
    Alert,
    Button
} from 'reactstrap'
import { Link } from 'react-router-dom';
import Header from '../components/Header'
import { emailRegex } from '../util/Patterns'
import API from '../api/api'

const taskAPI = new API({ url: process.env.REACT_APP_FLASK_API_URL, name: 'api/upload' })

class Upload extends Component {
    constructor() {
        super()
        this.state = {
            email: '',
            processed: false,
            task_id: '',
            keywords: []
        }
        this.handleSubmit = this.handleSubmit.bind(this)
    }
    handleSubmit(event) {
        event.preventDefault() 
        let formData = new FormData(event.target)
        taskAPI.endpoints.putFile({ formData: formData })
			.then((res) => { 
                this.setState({ 
                    processed: true,
                    task_id: res.data.id,
                    keywords: res.data.keywords
                })
            })
			.catch((error) => { console.log(error) })
    }
    render() {
        const keywordsList = this.state.keywords.map((keyword, i) => {
			return (
            <ListGroup key={i}>
                <ListGroupItem>
                { keyword }
                </ListGroupItem>
            </ListGroup>
            )
        })
        return (
          <Container>
            <Header title={"Resume Upload"} back={""} />
            <Form onSubmit={this.handleSubmit} >
                <FormGroup>
                    <Label for="email">Email address (For job suggestions)</Label>
                    <Input type="email" name="email" id="email" pattern={emailRegex} required />
                </FormGroup>
                <FormGroup>
                    <Label for="file">Resume in .doc/.docx</Label>
                    <Input type="file" name="file" id="file" accept=".docx,.doc" required />
                </FormGroup>
                <Button color="secondary">Send Me Recommendations Now</Button>
            </Form>
            <br />
            { this.state.processed ? <Alert color="success">Processed upload successfully 
                &nbsp;<Link to={`/task/${this.state.task_id}`}>View Task</Link></Alert> : ''}
            <br />
            { this.state.processed ? <h3>Keywords Extracted</h3> : ''}
            { keywordsList }
          </Container>
        )
    }
}
export default Upload;