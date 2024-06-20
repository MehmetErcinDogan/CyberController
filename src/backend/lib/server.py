import websockets
import asyncio


class Server:
    def __init__(self, port=9999) -> None:
        self._port = port
        self._WSclients = []
        self.__connectedUsers = []

    def _run(self):
        print(f"Server started to listening on \"localhost:{self._port}\"")
        serve = websockets.serve(self._clientHandler, "localhost", self._port)
        asyncio.get_event_loop().run_until_complete(serve)
        asyncio.get_event_loop().run_forever()

    async def _clientHandler(self, ws):
        print(f"Websocket client connected from {ws.remote_address}")
        self._WSclients.append(ws.remote_address)

        try:
            while True:
                msg = await ws.recv()
        except:
            pass


if __name__ == "__main__":
    s1 = Server()
    s1.run()
