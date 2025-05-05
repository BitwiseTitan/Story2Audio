import unittest
import grpc
import asyncio
from fastapi.testclient import TestClient


from app.main import app

import story_pb2, story_pb2_grpc

# FASTAPI TEST CASES
class TestFastAPIStoryGeneration(unittest.TestCase):
    client = TestClient(app)

    def test_generate_valid_topic(self):
        response = self.client.post("/generate", json={"topic": "Apocalypse"})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertTrue(len(data["story"]) > 10)
        self.assertTrue(data["audio_file"].endswith(".mp3"))

    def test_generate_missing_topic(self):
        response = self.client.post("/generate", json={})
        self.assertEqual(response.status_code, 422)

    def test_generate_empty_topic(self):
        response = self.client.post("/generate", json={"topic": ""})
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())

# gRPC TEST CASES
class TestgRPCStoryGeneration(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.channel = grpc.aio.insecure_channel("localhost:50051")
        self.stub = story_pb2_grpc.StoryGeneratorStub(self.channel)

    async def asyncTearDown(self):
        await self.channel.close()

    async def test_generate_valid_topic(self):
        request = story_pb2.StoryRequest(topic="Survival")
        response = await self.stub.Generate(request, timeout=30)
        self.assertTrue(response.story)
        self.assertTrue(response.audio_file)

    async def test_generate_empty_topic(self):
        request = story_pb2.StoryRequest(topic="")
        with self.assertRaises(grpc.aio.AioRpcError) as cm:
            await self.stub.Generate(request)
        self.assertEqual(cm.exception.code(), grpc.StatusCode.INVALID_ARGUMENT)

    async def test_concurrent_requests(self):
        topics = ["Apocalypse", "Love"]
        tasks = [self.stub.Generate(story_pb2.StoryRequest(topic=t)) for t in topics]
        responses = await asyncio.gather(*tasks)
        for res in responses:
            self.assertTrue(res.story)
            self.assertTrue(res.audio_file)

if __name__ == "__main__":
    unittest.main()
