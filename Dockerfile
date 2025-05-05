# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Expose ports for FastAPI and gRPC
EXPOSE 8000 50051

# Command to start both servers
CMD ["sh", "-c", "python grpc_server.py & uvicorn app.main:app --host 0.0.0.0 --port 8000"]
