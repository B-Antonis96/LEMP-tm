import React from 'react';
import './App.css';
import MessageList from './components/messageList';

///////////////
// MAIN: App //
///////////////
const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>{process.env.REACT_APP_TITLE}</h1>
        <MessageList />
      </header>
    </div>
  );
}

export default App;
