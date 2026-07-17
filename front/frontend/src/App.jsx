import Header from "./components/layout/Header";
import Sidebar from "./components/layout/Sidebar";
import ChatBox from "./components/chat/ChatBox";
import getSessionId from "./utils/session";

function App() {

  console.log(getSessionId());

  return (
    <div className="app">

      <Header />

      <div className="main-layout">

        <Sidebar />

        <ChatBox />

      </div>

    </div>
  );
}

export default App;