import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

import "./styles/layout.css";
import "./styles/sidebar.css";
import "./styles/upload.css";
import "./styles/chat.css";
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
