import websockets
import asyncio
import threading

class Server:
    def __init__(self,port) -> None:
        self._port = port
        self._WSclients = []
        self.__connectedUsers = []

    def run(self):
        print(f"Server started to listening on \"localhost:{self._port}\"")
        serve = websockets.serve(self._clientHandler,"localhost",self._port)
        asyncio.get_event_loop().run_until_complete(serve)
        asyncio.get_event_loop().run_forever()


    def _x(self):
        print(self._WSclients)

    async def _clientHandler(self,ws):
        print(f"Websocket client connected from {ws.remote_address}")
        self._WSclients.append(ws.remote_address)

        try:
            threading.Thread(target = self._x).run()
            while True:
                pass
        except:
            pass