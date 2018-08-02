import React, { Component } from 'react';
import { 
    Container, 
    Form, 
    FormGroup, 
    Label, 
    Input, 
    ListGroup, 
    ListGroupItem,
    Alert
} from 'reactstrap'
import { Link } from 'react-router-dom';
import Header from '../components/Header'
import ValidateEmail from '../util/EmailValidator'
import API from '../api/api'

const taskAPI = new API({ url: process.env.REACT_APP_FLASK_API_URL, name: 'api/upload' })

class Upload extends Component {
    constructor() {
        super()
        this.state = {
            email: '',
            processed: false,
            task_id: '',
            keywords: [],
            isValid: true
        }
        this.handleUpload = this.handleUpload.bind(this)
        this.handleEmail = this.handleEmail.bind(this)
    }
    handleEmail(email) {
        if (!email || !ValidateEmail(email)) {
            this.setState({ isValid: false });
            return;
        }
        this.setState({ email: email, isValid: true })
    }
    handleUpload(files) { 
        if (!files[0] || !this.state.isValid ) return;
        let formData = new FormData();
        formData.append('file', files[0])
        formData.append('email', this.state.email)
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
            <Form>
                <FormGroup>
                    <Label for="email">Email address (For job suggestions)</Label>
                    <Input type="email" name="email" id="email"
                        onChange={ (e) => this.handleEmail(e.target.value)} />
                </FormGroup>
                <FormGroup>
                    <Label for="file">Resume in .doc/.docx</Label>
                    <Input type="file" name="file" id="file"
                        onChange={ (e) => this.handleUpload(e.target.files)} />
                </FormGroup>
            </Form>
            { this.state.isValid ? '' : <Alert color="warning">Please enter a valid email address</Alert>}
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