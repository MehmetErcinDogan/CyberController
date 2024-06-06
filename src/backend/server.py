import asyncio
import traceback
import websockets

async def clientHandler(websocket):
    async for message in websocket:
        print(f"Message{message}")
        await websocket.send(message)


if __name__ == "__main__":
    server = websockets.serve(clientHandler,"localhost",5000)
    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()
