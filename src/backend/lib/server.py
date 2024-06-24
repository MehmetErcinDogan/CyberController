from dataclasses import dataclass
from lib.database import Database
import threading
import websockets
import datetime
import hashlib
import asyncio
import json
import time
import sys

# gonna complete the another script for scheduled tasks
# gonna complete db
# gonna complete the features


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
            self._db = Database("data")  # initialize or load database

        except Exception as e:
            print("Error occured during initialize server object as", e)
            sys.exit()

    def run(self):
        print(f"Server started to listening on \"localhost:{self._port}\"")
        server_thread = threading.Thread(target=self._run_server, daemon=True)
        server_thread.start()

        try:
            while True:
                command = input("Command: ").strip().upper()
                if command == "SHOW":
                    self._listClients()
                elif command == "EXIT":
                    sys.exit()

        except KeyboardInterrupt:
            print("Keyborad")
            sys.exit()

    # start server as application
    # starts serving at new thread

    async def _start_server(self):  # runs server
        serve = await websockets.serve(self._clientHandler, "localhost", self._port)
        await serve.wait_closed()
        # and when client connected adds one more client handler function for each client

    def _run_server(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self._start_server())
        # start server

    def _listClients(self):  # printing clients
        print("[", end=" ")

        for i in self._clients:
            print(i.id, end=" ")

        print("]")

    def _clientRemove(self, ws):  # remove client from clien list
        for i in self._clients:
            if i.ws == ws:
                self._clients.remove(i)
                return True
        return False

    # checks time out if user do not access more than 10 min, terminate that client
    def _timeoutCheck(self):
        for client in self._clients:
            if ((client.recentTime - time.time()) > (10*60)):
                client.ws.close()
                self._clients.remove(client)

    def _parser(msg):  # parse messages
        try:
            msg = msg.strip()
            if msg[0] != "#":
                raise Exception("Comming Message Error")
            else:
                _ = msg.split()
                if len(_) != 1:
                    ms = _[0]
                    tag = _[1:]
                else:
                    ms = _[0]
                    tag = []

                return (tag, ms)

        except Exception as e:
            print("Error occured at parser as", e)

    def _clientFindByID(self, id):
        for i in self._clients:
            if i.id == id:
                return i
        return False

    def _clientFindByWS(self, ws):
        for i in self._clients:
            if i.ws == ws:
                return i
        return False

    async def _clientHandler(self, ws):
        print(f"Websocket client connected from {ws.remote_address}")
        try:
            msg = await ws.recv()
            if (msg == "#INIT"):
                msg = await ws.recv()
                tag, msg = Server._parser(msg)
                await self._mssgHandler(tag, msg, ws)

        except websockets.ConnectionClosed:
            self._clientRemove(ws)
            print(f"WS Client from {ws.remote_address} disconnected")

        except Exception as e:
            print(f"Error occured at ws client {e} from {ws.remote_address}")

        finally:
            self._timeoutCheck()
            await ws.close()
            print(f"WS Connection closed {ws.remote_address}")

    async def _mssgHandler(self, tag, msg, ws):
        try:
            if msg == "#CHECK":  # CHECK id
                if len(tag) != 1:
                    raise Exception("Wrong tag value")

                else:
                    i = self._clientFindByID(tag[0])
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
                    print(username, password)
                    # if self._db.checkUser(username, password):
                    if username == "admin" and password == "admin":  # gonna remove
                        id = str(datetime.datetime.now())
                        id = id.encode()
                        id = hashlib.sha256(id)
                        id = id.hexdigest()

                        client = Client(ws, id, time.time(),
                                        username, password)

                        self._clients.append(client)
                        # creates client at above

                        await ws.send(f"#ALLOW {id}")
                        await self._connectedClient(ws)
                    else:
                        await ws.send("#DENY")

        except Exception as e:
            print("Error occured at msgHandler as", e)

    async def _connectedClient(self, ws):
        try:
            i = self._clientFindByWS(ws)
            while True:
                tag, msg = Server._parser(await ws.recv())
                print(msg)
                if msg == "#LISTDEVICES":
                    await ws.send(json.dumps([("192.168.1.1","ercin"),("192.168.1.2","can")]))
                elif msg == "#DDOS":
                    if len(tag) != 1:
                        raise ("Tag error from DDOS")
                    targetIP = tag[0]
                    # result = DDOS(targetIP)
                    result = []
                    ws.send(json.dump(result))

        except Exception as e:
            print("Error occured at connectedClient as", e)
