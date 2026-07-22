import axios from "axios";
import getSessionId from "../utils/session";

const BASE_URL = "http://127.0.0.1:8000";

export async function uploadPDF(file) {

    const formData = new FormData();

    formData.append("file", file);

    const response = await axios.post(

        `${BASE_URL}/upload`,

        formData,

        {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        }

    );

    return response.data;
}

export async function sendMessage(question, onChunk) {

    const response = await fetch(`${BASE_URL}/chat`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            question: question,
            session_id: getSessionId()
        })
    });

    if (!response.ok || !response.body) {
        throw new Error("Chat request failed");
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    let fullText = "";

    while (true) {

        const { done, value } = await reader.read();

        if (done) break;

        fullText += decoder.decode(value, { stream: true });

        onChunk(fullText);

    }

    return fullText;
}