import websockets
import asyncio
from database import Database
import sys
import time
from dataclasses import dataclass

@dataclass
class Client:
    ws:websockets
    id:hash
    recentTime :float
    username: str
    password:str

# gonna complete that class
# functions are going to check
# gonna complete db
# gonna complete changes about the client list
# gonna complete the features
# gonna complete the hash function
# gonna complete the features
# gonna complete the vue linkage
# gonna complete the another script for scheduled tasks
# gonna think about above task

class Server:
    def __init__(self, port=9999) -> None:
        try:
            self._port = port
            self._clients = []
            self._db = Database()

        except Exception as e:
            print("Error occured during initialize server object as", e)
            sys.exit()

    def _run(self):
        print(f"Server started to listening on \"localhost:{self._port}\"")
        serve = websockets.serve(self._clientHandler, "localhost", self._port)
        asyncio.get_event_loop().run_until_complete(serve)
        asyncio.get_event_loop().run_forever()

    async def _clientHandler(self, ws):
        print(f"Websocket client connected from {ws.remote_address}")
        client = Client(ws,id,time.time(),None,None)
        self._clients.append(client)
        print("All Ws Clients:",self._WSclients)
        try:
            msg = await ws.recv()
            tag, msg = await Server._parser()
            await self._mssgHandler(tag, msg, ws)
        except websockets.ConnectionClosed:
            self._WSclients.remove(ws)
            print(f"WS Client from {ws.remote_address} disconnected")
        except Exception as e:
            print(f"Error occured at ws client {e} from {ws.remote_address}")
        finally:
            # for id,lastTime in self._connectedID:
            #     if ((time.time()-lastTime)>(10*60)):
            #         self._connectedID.remove((id,lastTime))
            if ws in self._WSclients:
                self._WSclients.remove(ws)
                await ws.close()
                print(f"WS Connection closed {ws.remote_address}")

    async def _mssgHandler(self, tag, msg, ws):
        try:
            if msg == "#CHECK":
                if len(tag) != 1:
                    raise Exception("Wrong tag value")
                else:
                    try:
                        self._connectedID.index(tag[0])
                        await ws.send("#ALLOW")
                        await self._connectedClient(ws)
                    except ValueError:
                        await ws.send("#DENY")
            elif msg == "#SIGN":
                if len(tag) != 2:
                    raise Exception("Wrong tag value")
                else:
                    username = tag[0]
                    password = tag[1]
                    if self._db.checkUser(username, password):
                        # gonna create hash id and should add to list with last accsess time
                        await ws.send("#ALLOW")
                        await self._connectedClient(ws)
                    else:
                        await ws.send("#DENY")
        except Exception as e:
            print("Error occured at msgHandler as", e)

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

    async def _connectedClient(self, ws):
        try:
            while True:
                tag, msg = await Server._parser(ws.recv())
                if msg == "#as":
                    print("asdas")

        except Exception as e:
            print("Error occured at connectedClient as", e)
