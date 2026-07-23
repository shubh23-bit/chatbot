from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil

from app.ingestion.ingest_pipeline import ingest_pdf

router = APIRouter()

UPLOAD_DIR = Path("data/uploads")

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)


@router.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...)
    
):

    file_path = (
        UPLOAD_DIR /
        file.filename
    )
    print("shubha",file_path)
    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    result = ingest_pdf(
        str(file_path)
    )
    print("shubham",result)

    return {
        "message":
        f"{file.filename} uploaded successfully",
        "details": result
    }