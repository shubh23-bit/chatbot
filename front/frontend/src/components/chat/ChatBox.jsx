import { useState } from "react";
import ChatWindow from "./ChatWindow";
import { sendMessage } from "../../services/api";

function ChatBox() {

    const [messages, setMessages] = useState([
        {
            role: "assistant",
            text: "Hello 👋 Upload a PDF and ask me anything."
        }
    ]);

    const sendQuestion = async (question) => {

        if (!question.trim()) return;

        // Show user message immediately
        setMessages((prev) => [
            ...prev,
            {
                role: "user",
                text: question
            }
        ]);

        try {

            const response = await sendMessage(question);

            setMessages((prev) => [
                ...prev,
                {
                    role: "assistant",
                    text: response.answer
                }
            ]);

        }
        catch (error) {

            console.error(error);

            setMessages((prev) => [
                ...prev,
                {
                    role: "assistant",
                    text: "❌ Something went wrong."
                }
            ]);

        }

    };

    return (

        <ChatWindow
            messages={messages}
            sendMessage={sendQuestion}
        />

    );

}

export default ChatBox;