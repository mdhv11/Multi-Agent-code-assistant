import asyncio
import websockets


async def test_ws():
    uri = "ws://localhost:8000/ws/generate"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Write a Python script to find sum of first 10 odd numbers")
        try:
            while True:
                msg = await websocket.recv()
                print(msg)
        except websockets.ConnectionClosed:
            print("Connection closed")

asyncio.run(test_ws())
