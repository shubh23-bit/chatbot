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

    const [isLoading, setIsLoading] = useState(false);

    const updateLastMessage = (text) => {
        setMessages((prev) => {
            const updated = [...prev];
            updated[updated.length - 1] = { role: "assistant", text };
            return updated;
        });
    };

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

        // Placeholder assistant message, filled in as the stream arrives
        setMessages((prev) => [
            ...prev,
            {
                role: "assistant",
                text: ""
            }
        ]);

        setIsLoading(true);

        try {

            await sendMessage(question, updateLastMessage);

        }
        catch (error) {

            console.error(error);

            updateLastMessage("❌ Something went wrong.");

        }
        finally {

            setIsLoading(false);

        }

    };

    return (

        <ChatWindow
            messages={messages}
            sendMessage={sendQuestion}
            isLoading={isLoading}
        />

    );

}

export default ChatBox;
