import { useState } from "react";

function ChatInput({

  sendMessage,

  disabled

}) {

  const [question, setQuestion] = useState("");

  const handleSend = () => {

    if (!question.trim() || disabled) return;

    sendMessage(question);

    setQuestion("");

  };

  return (

    <div className="chat-input">

      <input

        type="text"

        placeholder="Ask anything about your PDF..."

        value={question}

        disabled={disabled}

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

        disabled={disabled || !question.trim()}

        aria-label="Send message"

      >

        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path
            d="M4 20l16-8L4 4v6l10 2-10 2v6z"
            fill="currentColor"
          />
        </svg>

      </button>

    </div>

  );

}

export default ChatInput;
