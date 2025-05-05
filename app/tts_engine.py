import edge_tts
import os
import uuid

async def synthesize_audio(text: str) -> str:
    output_dir = "static"
    os.makedirs(output_dir, exist_ok=True)

    file_name = f"{uuid.uuid4().hex}.mp3"
    path = os.path.join(output_dir, file_name)

    # Use a natural-sounding voice
    tts = edge_tts.Communicate(text, voice="en-US-AriaNeural")
    await tts.save(path)

    return path
