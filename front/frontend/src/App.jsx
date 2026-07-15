import ChatBox from "./components/ChatBox";
import getSessionId from "./utils/session";

function App() {
  console.log(
    getSessionId()
  );
  return (
    <div className="app">
      <h1>RAG Chatbot</h1>
      <ChatBox />
    </div>
  );
}

export default App;