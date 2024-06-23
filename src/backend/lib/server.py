from dataclasses import dataclass
from lib.database import Database
from lib.features import DDOS
import websockets
import datetime
import hashlib
import asyncio
import time
import json
import sys


# gonna complete the another script for scheduled tasks
# gonna think about above task

# gonna check all await functions and their await keywords
# gonna complete db
# gonna complete the vue linkage
# gonna complete the features

# gonna add comment lines
# make it more readable


@dataclass
class Client:  # Stores client datas
    ws: None  # websocket
    id: int  # stores id for when ws changed, should be check is logged in or not
    recentTime: float  # stores last accessed time for time out
    username: str  # stores username of client
    password: str  # store password of client


class Server:
    def __init__(self, port=9999) -> None:
        try:
            self._port = port
            self._clients = []
            # self._db = Database("../data/")  # initialize or load database

        except Exception as e:
            print("Error occured during initialize server object as", e)
            sys.exit()

    def run(self):  # runs server
        print(f"Server started to listening on \"localhost:{self._port}\"")
        serve = websockets.serve(self._clientHandler, "localhost", self._port)
        asyncio.get_event_loop().run_until_complete(serve)
        asyncio.get_event_loop().run_forever()
        # start server app and when client connected adds one more client handler function for each client

    async def _listClients(self):  # printing clients
        print("[", end=" ")

        for i in self._clients:
            print(i.id, end=" ")

        print("]")

    async def _clientRemove(self, ws):  # remove client from clien list
        for i in self._clients:
            if i.ws == ws:
                self._clients.remove(i)
                return True
        return False

    # checks time out if user do not access more than 10 min, terminate that client
    async def _timeoutCheck(self):
        for client in self._clients:
            if ((client.recentTime - time.time()) > (10*60)):
                client.ws.close()
                self._clients.remove(client)

    async def _parser(msg):  # parse messages
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

    async def _clientFindByID(self,id):
        for i in self._clients:
            if i.id == id:
                return i
        return False

    async def _clientFindByWS(self,ws):
        for i in self._clients:
            if i.ws == ws:
                return i
        return False
    
    async def _clientHandler(self, ws):
        print(f"Websocket client connected from {ws.remote_address}")
        try:
            msg = await ws.recv()
            tag, msg = await Server._parser(msg)
            await self._mssgHandler(tag, msg, ws)

        except websockets.ConnectionClosed:
            await self._clientRemove(ws)
            print(f"WS Client from {ws.remote_address} disconnected")

        except Exception as e:
            print(f"Error occured at ws client {e} from {ws.remote_address}")

        finally:
            await self._timeoutCheck()
            await self._clientRemove(ws)
            await ws.close()
            print(f"WS Connection closed {ws.remote_address}")

    async def _mssgHandler(self, tag, msg, ws):  # complete
        try:
            if msg == "#CHECK":  # CHECK id
                if len(tag) != 1:
                    raise Exception("Wrong tag value")

                else:
                    i = await self._clientFindByID(tag[0])
                    if i != False:
                        await ws.send("#ALLOW")
                        i.ws = ws
                        i.recentTime = time.time()
                        await self._connectedClient(ws)
                    else:
                        await ws.send("#DENY")

            elif msg == "#SIGN":  # SIGN username password
                if len(tag) != 2:
                    raise Exception("Wrong tag value")

                else:
                    username = tag[0]
                    password = tag[1]
                    if self._db.checkUser(username, password):
                        # gonna create hash id and should add to list with last accsess time
                        # complete

                        id = str(datetime.datetime.now())
                        id = id.encode()
                        id = hashlib.sha256(id)
                        id = id.hexdigest()

                        client = Client(ws, id, time.time(), username, password)

                        self._clients.append(client)
                        await self._listClients()
                        # creates and lists clients at above

                        await ws.send("#ALLOW")
                        await self._connectedClient(ws)  # change
                    else:
                        await ws.send("#DENY")

        except Exception as e:
            print("Error occured at msgHandler as", e)

    async def _connectedClient(self, ws):  # gonna complete
        try:
            i = self._clientFindByWS(ws)
            while True:
                tag, msg = await Server._parser(ws.recv())

                if msg == "#DDOS":
                    if len(tag) != 1:
                        raise("Tag error from DDOS")
                    targetIP = tag[0]
                    # result = DDOS(targetIP)
                    result = []
                    ws.send(json.dump(result))
                    

        except Exception as e:
            print("Error occured at connectedClient as", e)
