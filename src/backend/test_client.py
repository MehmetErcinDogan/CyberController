import websockets
import asyncio

async def client():
    async with websockets.connect("ws://localhost:9999") as ws:
        while True:
            await ws.send("hi")
            print("sended")
            

asyncio.run(client())