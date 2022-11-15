import React from 'react';
import './App.css';
import MessageList from './components/messageList';

// Declaring title for page
let appTitle = process.env.REACT_APP_TITLE;
let title = appTitle ? appTitle : 'Welkom bij mijn eindopdracht!';

///////////////
// MAIN: App //
///////////////
const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>{title}</h1>
        <MessageList />
      </header>
    </div>
  );
}

export default App;
