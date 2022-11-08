import React from "react";

import axios from 'axios';

export default class MessageList extends React.Component {
  state = {
    messages: []
  }

  componentDidMount() {
    axios(`http://127.0.0.1:8000/messages`, {
      method: 'GET'
    }).then(response => {
        const messages = response.data;
        this.setState({ messages });
      })
  }

  render() {
    const divStyle = {
        borderColor: 'coral'
    }
    const senderStyle = {
        color: 'red'
    }
    return (
        this.state.messages.map(
            message => 
                <div key={message['id']} style={divStyle}>
                    <p style={senderStyle}>{message['sender']}</p>
                    <p> {message['text']}</p>
                </div>
        )
    );
  }
}