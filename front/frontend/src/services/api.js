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

export async function sendMessage(question) {

    const response = await axios.post(

        `${BASE_URL}/chat`,

        {
            question: question,
            session_id: getSessionId()
        }

    );

    return response.data;
}