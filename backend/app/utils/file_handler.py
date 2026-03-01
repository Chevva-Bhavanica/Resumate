# app/utils/file_handler.py

import os
import shutil
from fastapi import UploadFile
from uuid import uuid4

UPLOAD_DIR = "uploads/resumes"

# Ensure upload folder exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

# --------------------------------------------------
# Save uploaded file
# --------------------------------------------------
def save_file(file: UploadFile) -> str:
    """
    Saves an uploaded file to UPLOAD_DIR with a unique name
    Returns the file path
    """
    ext = file.filename.split(".")[-1]
    filename = f"{uuid4().hex}.{ext}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_path


# --------------------------------------------------
# Delete file
# --------------------------------------------------
def delete_file(file_path: str):
    if os.path.exists(file_path):
        os.remove(file_path)
