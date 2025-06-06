# Dockerfile.dev - Development Dockerfile for building and running the FastAPI
# Source-to-Pay (S2P) app in a lightweight Python container with live-reloading
# support via Uvicorn.

# Use the official Python 3.12 slim image as the base
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY . .

# Set the default command to run the FastAPI app with uvicorn
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000","--reload"]
