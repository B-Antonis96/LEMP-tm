import { env } from 'process';
import React from 'react';
import './App.css';
import MessageList from './components/messageList';

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Welkom bij mijn eindopdracht!</h1>
        <MessageList />
      </header>
    </div>
  );
}

export default App;
