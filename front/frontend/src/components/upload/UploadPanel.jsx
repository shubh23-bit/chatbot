import { useState } from "react";
import { uploadPDF } from "../../services/api";

function UploadPanel() {

    const [file, setFile] = useState(null);

    const [status, setStatus] = useState("No file uploaded");

    const handleUpload = async () => {

        if (!file) {

            setStatus("Please select a PDF.");

            return;

        }

        try {

            const response = await uploadPDF(file);

            setStatus(response.message);

        }

        catch (error) {

            console.error(error);

            setStatus("Upload Failed");

        }

    };

    return (

        <div className="upload-panel">

            <h2>📂 Upload PDF</h2>

            <p>Select a PDF to start chatting.</p>

            <input

                type="file"

                accept=".pdf"

                onChange={(e) =>

                    setFile(e.target.files[0])

                }

            />

            <button onClick={handleUpload}>

                Upload

            </button>

            <div className="upload-status">

                {status}

            </div>

        </div>

    );

}

export default UploadPanel;