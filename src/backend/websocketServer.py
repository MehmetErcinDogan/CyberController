import asyncio
import websockets

async def server(websocket,path):
    async for message in websocket:
        await websocket.send(f"Got your msg:{message}")
    
start_server = websockets.serve(server,"localhost",5000)

print("Server Started . . .")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()