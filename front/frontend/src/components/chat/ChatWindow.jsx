import MessageList from "./MessageList";
import ChatInput from "./ChatInput";

function ChatWindow({

  messages,

  sendMessage,

  isLoading

}) {

  return (

    <section className="chat-window">

      <MessageList

        messages={messages}

      />

      <ChatInput

        sendMessage={sendMessage}

        disabled={isLoading}

      />

    </section>

  );

}

export default ChatWindow;
