import { useState } from "react";
import axios from "axios";
import ChatInput from "./ChatInput";
import Message from "./Message";

function ChatBox() {
  const [messages, setMessages] = useState([]);

  const sendMessage = async (question) => {
    if (!question.trim()) return;

    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        text: question,
      },
    ]);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/chat",
        {
          question,
        }
      );

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: response.data.answer,
        },
      ]);
    } catch (error) {
      console.log(error);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: "Something went wrong.",
        },
      ]);
    }
  };

  return (
    <>
      <div className="chat-container">
        {messages.map((msg, index) => (
          <Message
            key={index}
            role={msg.role}
            text={msg.text}
          />
        ))}
      </div>

      <ChatInput sendMessage={sendMessage} />
    </>
  );
}

export default ChatBox;