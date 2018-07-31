import React from 'react';
import { Container, Card, CardText, Button, ButtonGroup } from 'reactstrap'
import { Link } from 'react-router-dom';

const Home = () => (
  <div>
    <Container>
        <div className="text-center">
        <Card body >
            <h2>Welcome</h2>
            <CardText>View one of the main items to get started</CardText>
            <ButtonGroup>
                <Link to={'/upload/'}><Button>Upload Resume Job Suggestions</Button></Link>
                &nbsp;
                <Link to={'/tasks'}><Button>View Processing Tasks</Button></Link>
            </ButtonGroup>
        </Card>
        </div>
    </Container>
  </div>
)
export default Home;
