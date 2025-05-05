import gradio as gr
import grpc
import story_pb2
import story_pb2_grpc

def get_story(topic):
    try:
        with grpc.insecure_channel("localhost:50051") as channel:
            stub = story_pb2_grpc.StoryGeneratorStub(channel)
            request = story_pb2.StoryRequest(topic=topic)
            response = stub.Generate(request)
            return response.story, response.audio_file
    except Exception as e:
        return f"Error: {e}", None

gr.Interface(
    fn=get_story,
    inputs=gr.Textbox(label="Enter a topic", placeholder="e.g. apocalypse, monarchy"),
    outputs=[
        gr.Textbox(label="Generated Story"),
        gr.Audio(label="Narration", type="filepath")  # Streams inline & allows download
    ],
    title="gRPC Story Generator"
).launch()
