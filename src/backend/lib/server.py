import websockets
import asyncio
from database import Database
import sys

class Server:
    def __init__(self, port=9999) -> None:
        try:
            self._port = port
            self._WSclients = []
            self._connectedID = []
            self._db = Database()
        except Exception as e:
            print("Error occured during initialize server object as",e)
            sys.exit()
            
    def _run(self):
        print(f"Server started to listening on \"localhost:{self._port}\"")
        serve = websockets.serve(self._clientHandler, "localhost", self._port)
        asyncio.get_event_loop().run_until_complete(serve)
        asyncio.get_event_loop().run_forever()

    async def _clientHandler(self, ws):
        print(f"Websocket client connected from {ws.remote_address}")
        self._WSclients.append(ws.remote_address)

        try:
            run = True
            while run:
                msg = await ws.recv()
                tag, msg = await Server._parser()
                run = await self._mssgHandler(tag, msg, ws)
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

    async def _mssgHandler(self, tag, msg, ws): # NOT FİNİSHED
        try:
            if msg == "#CHECK":
                if len(tag) != 1:
                    raise Exception("Wrong tag value")
                else:
                    try:
                        self._connectedID.index(tag[0])
                        await ws.send("#ALLOW")
                        return True
                    except ValueError:
                        await ws.send("#DENY")
                        return False
            elif msg == "#SIGN":
                username = tag[0]
                password = tag[1]
                if self._db.checkUser(username,password):
                    await ws.send("#ALLOW")
                    return True
                else:
                    await ws.send("#DENY")
                    return False
                
        except Exception as e:
            print("Error occured at msgHandler as", e)
            return False
        
    async def _parser(msg):
        try:
            msg = msg.strip()
            if msg[0] != "#":
                raise Exception("Comming Message Error")
            else:
                _ = msg.find(' ')
                ms = msg[:_].strip().upper()
                tag = msg[_+1, :].strip().split()
                return (tag, ms)
        except Exception as e:
            print("Error occured at parser as", e)


if __name__ == "__main__":
    s1 = Server()
    s1.run()
