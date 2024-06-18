import asyncio
import websockets

async def clientHandler(ws):
    try:
        while True:
            msg = await ws.recv()
            await ws.send(msg[::-1])
    except websockets.ConnectionClosedError:
        print("Connection closed")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    server = websockets.serve(clientHandler,"localhost",5000)
    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()
