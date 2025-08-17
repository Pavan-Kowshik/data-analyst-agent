import tempfile
import zipfile
import tarfile
import os
import subprocess
import sys
import json
from fastapi import FastAPI, Request, UploadFile
from fastapi.responses import JSONResponse
import uvicorn
import base64
import io
from dotenv import load_dotenv
import openai

load_dotenv()
app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.base_url = os.getenv("OPENAI_BASE_URL")
LLM_MODEL = os.getenv("LLM_MODEL")

def get_content_type_for_image(filename):
    ext = filename.lower().split('.')[-1]
    if ext in ["jpg", "jpeg"]:
        return "image/jpeg"
    elif ext == "png":
        return "image/png"
    elif ext == "gif":
        return "image/gif"
    else:
        return "application/octet-stream"

class FileData:
    def __init__(self, name, content, content_type, is_image=False, is_text=False):  # Fixed __init__
        self.name = name
        self.content = content
        self.content_type = content_type
        self.is_image = is_image
        self.is_text = is_text

# ... rest of your code ...

if __name__ == "__main__":  # Fixed __name__
    uvicorn.run(app, host="0.0.0.0", port=8000)
