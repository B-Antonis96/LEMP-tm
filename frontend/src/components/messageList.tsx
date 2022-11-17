import React from "react";
import axios from 'axios';

//////////////////////
// COM: MessageList //
//////////////////////
export default class MessageList extends React.Component {
  state = {
    messages: []
  }

  hostIn = process.env.REACT_APP_BACKEND;
  host = (this.hostIn !== undefined && this.hostIn !== null ? this.hostIn : 'localhost:8000');
  

  // On mount execute GET messages request
  componentDidMount() {
    axios('http://' + this.host + '/messages', {
      method: 'GET'
    }).then(response => {
        const messages = response.data;
        this.setState({ messages });
      })
  }

  // Render the React Component
  render() {
    const senderStyle = {
        color: 'red'
    }
    return (
      // Foreach message in state, map to html object
        this.state.messages.map(
            message => 
                <div key={message['id']}>
                    <p style={senderStyle}>{message['sender']}</p>
                    <p> {message['text']}</p>
                </div>
        )
    );
  }
}