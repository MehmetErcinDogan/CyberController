import asyncio
import websockets

async def test():
    while True:
        async with websockets.connect("ws://localhost:5000") as ws:
            await ws.send("asd")
    
asyncio.get_event_loop().run_until_complete(test())