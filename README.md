#  Story2Audio: Multimodal Story Generator

This project is a microservice-based NLP application that generates creative stories from a given topic and narrates them using text-to-speech. It includes:

-  FastAPI REST endpoint (`/generate`)
-  gRPC endpoint for high-performance interservice calls
-  Text generation using Hugging Face models
-  TTS audio synthesis
-  Tests for both REST and gRPC interfaces
-  Gradio UI + Postman testing
-  Dockerized for easy deployment

---

## Features

- **gRPC + FastAPI** microservices
- **Async concurrency** and parallel request handling
- **Error handling** for invalid topics and internal issues
- **Streaming and downloadable audio** output
- **Unit tests** for REST and gRPC interfaces
- **Frontend UI** with Gradio
- **Dockerized Deployment**

---

## Requirements

```bash
pip install -r requirements.txt
````

Key packages:

- `transformers`
- `torch`
- `fastapi`
- `uvicorn`
- `gradio`
- `grpcio`
- `grpcio-tools`
- `pydantic`
- `requests`
- `edge-tts`
- `uuid`
- `asyncio`


---

##  Usage

### FastAPI

```bash
uvicorn app.main:app --reload
```

### gRPC

```bash
python grpc_server.py
```

### Run Tests

```bash
python tests/test_fastapi.py
python tests/test_grpc.py
```

Or run both via:

```bash
run_tests.bat
```

### Gradio UI

```bash
python gradio_app.py
```

---

## API Reference

### POST `/generate` (FastAPI)

```json
{
  "topic": "Apocalypse"
}
```

**Response**:

```json
{
  "status": "success",
  "story": "...",
  "audio_file": "static/xyz.mp3"
}
```

### gRPC Method: `Generate(StoryRequest)`

```proto
message StoryRequest {
  string topic = 1;
}
message StoryReply {
  string story = 1;
  string audio_file = 2;
}
```

---

## Docker

### Build

```bash
docker build -t storygen-app .
```

### Run

```bash
docker run -p 8000:8000 -p 50051:50051 storygen-app
```

---

## Sample UI (Gradio)

The Gradio interface allows:

* Topic input
* Inline audio streaming
* Downloadable MP3 file

---

## Credits

Created by Talha Syed — BS Artificial Intelligence (2025)
Course: Fundamentals of NLP (AI4001 / CS4063)

---

## License

This project is academic-only and for educational use.

