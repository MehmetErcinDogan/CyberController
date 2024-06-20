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
                if msg.lower() == "#EXIT": # msg handlerin geriye döünüşü ile bağlantı kurmaya bak
                    print("WS connection closed",ws.remote_address)
                    self._WSclients.remove(ws)
                    await ws.close()
                    
                
                await self._mssgHandler(msg)

        except websockets.ConnectionClosed:
            self._WSclients.remove(ws)
            print(f"WS Client from {ws.remote_address} disconnected")
        except Exception as e:
            print(f"Error occured at ws client {e} from {ws.remote_address}")
        finally:
            if ws in self._WSclients:
                self._WSclients.remove(ws)
                await ws.close()
                print(f"WS Connection closed {ws.remote_address}")

    async def _mssgHandler(self,msg):
        return

if __name__ == "__main__":
    s1 = Server()
    s1.run()
