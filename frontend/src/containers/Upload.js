import React, { Component } from 'react';
import { 
    Container, 
    Form, 
    FormGroup, 
    Label, 
    Input, 
    ListGroup, 
    ListGroupItem
} from 'reactstrap'
import Header from '../components/Header'
import API from '../api/api'

const taskAPI = new API({ url: process.env.REACT_APP_API_URL, name: 'api/upload' })

class Upload extends Component {
    constructor() {
        super()
        this.state = {
            processed: false,
            task_id: '',
            keywords: []
        }
        this.handleUpload = this.handleUpload.bind(this)
    }
    handleUpload(files) { 
        if (files[0] == null) return;
        let formData = new FormData();
        formData.append('file', files[0])
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
                    <Label for="file">Resume in .doc/.docx</Label>
                    <Input type="file" name="file" id="file"
                        onChange={ (e) => this.handleUpload(e.target.files)} />
                </FormGroup>
            </Form>
            <p>{ this.state.processed ? 'Processed upload successfully' : ''}</p>
            <br />
            { this.state.processed ? <h3>Keywords Extracted</h3> : ''}
            { keywordsList }
          </Container>
        )
    }
}
export default Upload;