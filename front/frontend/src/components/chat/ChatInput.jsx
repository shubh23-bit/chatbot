import { useState } from "react";

function ChatInput({

  sendMessage

}) {

  const [question, setQuestion] = useState("");

  const handleSend = () => {

    sendMessage(question);

    setQuestion("");

  };

  return (

    <div className="chat-input">

      <input

        type="text"

        placeholder="Ask anything about your PDF..."

        value={question}

        onChange={(e) =>

          setQuestion(e.target.value)

        }

        onKeyDown={(e) => {

          if (e.key === "Enter") {

            handleSend();

          }

        }}

      />

      <button

        onClick={handleSend}

      >

        Send

      </button>

    </div>

  );

}

export default ChatInput;