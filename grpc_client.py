import grpc
import story_pb2
import story_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = story_pb2_grpc.StoryGeneratorStub(channel)
    request = story_pb2.StoryRequest(topic="Apocalypse")
    response = stub.GenerateStory(request)
    print("Generated Story:", response.story)

if __name__ == "__main__":
    run()
