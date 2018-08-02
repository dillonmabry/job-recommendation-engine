import React from 'react';
import { 
    Card, 
    CardHeader
} from 'reactstrap'

const footerStyle = {
    textAlign: "center",
    position: "fixed",
    bottom: "0",
    width: "100%",
}

const Footer = (props) => (
    <div style={footerStyle}>
        <br />
        <Card>
            <CardHeader>Check Out Other Projects!
                &nbsp;<a href="https://github.com/dillonmabry">GitHub</a>
            </CardHeader>
        </Card>
    </div>
)

export default Footer;