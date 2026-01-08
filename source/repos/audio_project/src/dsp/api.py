# api.py
from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
import uuid
import os
import json
import boto3
import tempfile
from src.dsp.features import extract_features
import pathlib

app = FastAPI()

# Templates directory
BASE_DIR = pathlib.Path(__file__).resolve().parent  # folder containing api.py
TEMPLATES_DIR = BASE_DIR / "templates"  # templates folder next to api.py
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

# AWS S3 client (keep for future deployment)
s3 = boto3.client("s3")
BUCKET = os.environ.get("AUDIO_BUCKET", "audio-analysis-michael-0724")

@app.get("/")
def home(request: Request):
    """Serve the Bulma frontend"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze")
async def analyze_audio(file: UploadFile = File(...)):
    # Validate file type
    if not file.filename.lower().endswith((".wav", ".mp3", ".aac", ".flac")):
        raise HTTPException(status_code=400, detail="Unsupported file type")

    # Get OS temp folder (works on Windows and Linux)
    tmp_dir = tempfile.gettempdir()
    tmp_path = os.path.join(tmp_dir, f"{uuid.uuid4()}-{file.filename}")

    try:
        # Save uploaded bytes to temp file
        with open(tmp_path, "wb") as f:
            contents = await file.read()
            f.write(contents)

        # Run BPM / feature extraction
        features = extract_features(tmp_path)

        # Upload results to S3
        result_key = f"processed/{os.path.basename(tmp_path)}.json"
        s3.put_object(Bucket=BUCKET, Key=result_key, Body=json.dumps(features))

        return {
            "status": "success",
            "features": features,
            "stored_at": result_key
        }

    except Exception as e:
        print("ERROR in /analyze:", e)
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        # Always delete temp file to prevent disk fill-up
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
