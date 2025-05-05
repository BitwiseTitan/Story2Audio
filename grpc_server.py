import grpc
from concurrent import futures
import asyncio
import story_pb2
import story_pb2_grpc
from app.story_generator import generate_story
from app.tts_engine import synthesize_audio
import os

class StoryService(story_pb2_grpc.StoryGeneratorServicer):
    def Generate(self, request, context):
        try:
            topic = request.topic.strip()
            if not topic:
                context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Topic cannot be empty")

            story = generate_story(topic)
            audio_path = asyncio.run(synthesize_audio(story))

            return story_pb2.StoryReply(
                status="success",
                story=story,
                audio_file=audio_path
            )
        except grpc.RpcError:
            raise  # Already handled by context.abort
        except Exception as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return story_pb2.StoryReply(status="error")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    story_pb2_grpc.add_StoryGeneratorServicer_to_server(StoryService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server started on port 50051.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
