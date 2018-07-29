import React from 'react';
import { Button, Container } from 'reactstrap'
import { Link } from 'react-router-dom';

const Header = ({ title, back }) => (
  <div>
    <Container>
        <Link to={`/${back}`}><Button color="light">Back</Button></Link>
        <h2 className="text-center">{ title }</h2>
    </Container>
    <hr />
  </div>
)

export default Header;