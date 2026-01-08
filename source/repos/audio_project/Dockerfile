FROM python:3.10-slim

# Prevents Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# System deps needed for librosa + soundfile
RUN apt-get update && apt-get install -y \
    build-essential \
    ffmpeg \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python deps first (Docker cache magic)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#install extra dependencies 
COPY requirements-extra.txt .
RUN pip install --no-cache-dir -r requirements-extra.txt

# Copy source code
COPY src ./src

# exit command for test container build
#CMD ["python", "-m", "src.dsp.ecs_run"]


#exit command for running api container build
# Expose port for API
EXPOSE 8000

# Start FastAPI server when container runs
CMD ["uvicorn", "src.dsp.api:app", "--host", "0.0.0.0", "--port", "8000"]

