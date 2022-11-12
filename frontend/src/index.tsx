import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

// Declaring title for tab
let title = process.env.REACT_APP_NAME;
document.title = title ? title : 'Undefined';

// Declaring root for ReactDOM
const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
