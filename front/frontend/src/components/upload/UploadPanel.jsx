import { useState } from "react";
import { uploadPDF } from "../../services/api";

function UploadPanel() {

    const [file, setFile] = useState(null);

    const [status, setStatus] = useState("No file uploaded yet.");
    const [statusType, setStatusType] = useState("idle");

    const handleUpload = async () => {

        if (!file) {

            setStatus("Please select a PDF first.");
            setStatusType("error");

            return;

        }

        setStatus("Uploading and indexing your PDF...");
        setStatusType("loading");

        try {

            const response = await uploadPDF(file);

            setStatus(response.message);
            setStatusType("success");

        }

        catch (error) {

            console.error(error);

            setStatus("Upload failed. Please try again.");
            setStatusType("error");

        }

    };

    return (

        <div className="upload-panel">

            <h2>📂 Upload PDF</h2>

            <p>Select a PDF to start chatting with it.</p>

            <label className="upload-dropzone">

                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M12 16V4m0 0L7 9m5-5l5 5M5 20h14"
                        stroke="currentColor"
                        strokeWidth="1.8"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                    />
                </svg>

                {file
                    ? <span className="filename">{file.name}</span>
                    : <span className="hint">Click to choose a PDF</span>
                }

                <input
                    type="file"
                    accept=".pdf"
                    onChange={(e) =>
                        setFile(e.target.files[0])
                    }
                />

            </label>

            <button
                className="upload-button"
                onClick={handleUpload}
                disabled={statusType === "loading"}
            >
                Upload
            </button>

            <div className={`upload-status ${statusType}`}>
                {status}
            </div>

        </div>

    );

}

export default UploadPanel;
