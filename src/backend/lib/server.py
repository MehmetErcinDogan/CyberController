import websockets
import asyncio
from database import Database
import sys
import time
from dataclasses import dataclass
import hashlib
import datetime


@dataclass
class Client:
    ws: websockets.legacy.server.WebSocketServerProtocol
    id: int
    recentTime: float
    username: str
    password: str

# gonna complete db
# gonna complete the vue linkage
# gonna complete the features
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

    async def _listClients(self):
        print("[", end=" ")
        for i in self._clients:
            print(i.id, end=" ")
        print("]")

    async def _clientRemove(self, ws):
        for i in self._clients:
            if i.ws == ws:
                self._clients.remove(i)
                break

    async def _clientFind(self, ws):
        for i in self._clients:
            if i.ws == ws:
                return i
        return False

    async def _timeoutCheck(self):
        for client in self._clients:
            if ((client.recentTime - time.time()) > (10*60)):
                client.ws.close()
                self._clients.remove(client)

    async def _clientHandler(self, ws):
        print(f"Websocket client connected from {ws.remote_address}")

        id = str(datetime.datetime.now())
        id = id.encode()
        id = hashlib.sha256(id)
        id = id.hexdigest()

        client = Client(ws, id, time.time(), None, None)

        self._clients.append(client)
        await self._listClients()

        try:
            msg = await ws.recv()
            tag, msg = await Server._parser()
            await self._mssgHandler(tag, msg, ws)

        except websockets.ConnectionClosed:
            await self._clientRemove(ws)
            print(f"WS Client from {ws.remote_address} disconnected")

        except Exception as e:
            print(f"Error occured at ws client {e} from {ws.remote_address}")
        finally:
            await self._timeoutCheck()
            result = await self._clientFind(ws)
            if result != False:
                self._clientRemove(ws)
                await ws.close()
                print(f"WS Connection closed {ws.remote_address}")

    async def _mssgHandler(self, tag, msg, ws): # complete
        try:
            if msg == "#CHECK":
                if len(tag) != 1:
                    raise Exception("Wrong tag value")
                else:
                    try:
                        self._connectedID.index(tag[0])  # change
                        await ws.send("#ALLOW")
                        await self._connectedClient(ws)  # change
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
                        # complete
                        await ws.send("#ALLOW")
                        await self._connectedClient(ws)  # change
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

    async def _connectedClient(self, ws):  # gonna complete
        try:
            while True:
                tag, msg = await Server._parser(ws.recv())
                if msg == "#as":
                    print("asdas")

        except Exception as e:
            print("Error occured at connectedClient as", e)
