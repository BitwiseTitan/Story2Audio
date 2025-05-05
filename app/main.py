from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.story_generator import generate_story
from app.tts_engine import synthesize_audio
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Story2Audio", version="1.0")

app.mount("/static", StaticFiles(directory="static"), name="static")

class StoryRequest(BaseModel):
    topic: str

@app.post("/generate")
async def generate(request: StoryRequest):
    try:
        story_text = generate_story(request.topic)
        audio_path = await synthesize_audio(story_text)

        return {
            "status": "success",
            "story": story_text,
            "audio_file": audio_path
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
