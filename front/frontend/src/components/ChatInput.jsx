import { useState } from "react";

function ChatInput({ sendMessage }) {
  const [question, setQuestion] = useState("");

  const handleSubmit = () => {
    sendMessage(question);
    setQuestion("");
  };

  return (
    <div className="input-box">
      <input
        value={question}
        onChange={(e) =>
          setQuestion(e.target.value)
        }
        placeholder="Ask something..."
      />

      <button onClick={handleSubmit}>
        Send
      </button>
    </div>
  );
}

export default ChatInput;