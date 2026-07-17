import MessageList from "./MessageList";
import ChatInput from "./ChatInput";

function ChatWindow({

  messages,

  sendMessage

}) {

  return (

    <section className="chat-window">

      <MessageList

        messages={messages}

      />

      <ChatInput

        sendMessage={sendMessage}

      />

    </section>

  );

}

export default ChatWindow;