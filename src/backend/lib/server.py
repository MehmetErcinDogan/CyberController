from dataclasses import dataclass
from lib.database import Database
import lib.features
import websockets
import threading
import datetime
import hashlib
import asyncio
import socket
import json
import time
import sys
import os

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

        except Exception as e:
            print("Error occured during initialize server object as", e)
            sys.exit()

    def run(self):
        print(
            f"Server started to listening on \"{socket.gethostbyname(socket.gethostname())}:{self._port}\"")
        # f"Server started to listening on localhost:\\",{self._port})

        server_thread = threading.Thread(target=self._run_server, daemon=True)
        server_thread.start()

        try:
            while True:
                command = input("Command: ").strip().upper()
                if command == "SHOW":
                    self._listClients()
                elif command == "EXIT":
                    sys.exit()
                elif command == "CLS":
                    os.system("cls")
                    print(
                        f"Server started to listening on \"{socket.gethostbyname(socket.gethostname())}:{self._port}\"")
                elif command == "KICK":
                    try:
                        ind = int(input("Index:"))
                        self._clients.pop(ind)
                    except Exception as e:
                        print("Error at KICK as", e)
        except KeyboardInterrupt:
            print("Keyborad Interrupt")
            sys.exit()

    # start server as application
    # starts serving at new thread

    async def _start_server(self):  # runs server
        serve = await websockets.serve(self._clientHandler, socket.gethostbyname(socket.gethostname()), self._port)
        # serve = await websockets.serve(self._clientHandler, "localhost", self._port)
        await serve.wait_closed()
        # and when client connected adds one more client handler function for each client

    def _run_server(self):
        self._db = Database("data")  # initialize or load database
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self._start_server())
        # start server

    def _listClients(self):  # printing clients
        print("[", end=" ")

        for i in self._clients:
            print("Address:", i.ws.remote_address, end="\t")
            print("ID:", i.id, end=" ,\n")

        print("]")

    def _clientRemove(self, ws):  # remove client from clien list
        for i in self._clients:
            if i.ws == ws:
                self._clients.remove(i)
                print("Clients removed")
                return True
        return False

    # checks time out if user do not access more than 10 min, terminate that client
    def _timeoutCheck(self):
        for client in self._clients:
            if ((client.recentTime - time.time()) > (10*60)):
                self._clients.remove(client)
                client.ws.close()

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

            elif msg == "#SIGN":  # SIGN with username password
                if len(tag) != 2:
                    raise Exception("Wrong tag value")

                else:
                    username = tag[0]
                    password = tag[1]
                    if self._db.checkUser(username, password):
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
                if i not in self._clients:
                    self._clientRemove()
                    await ws.close()
                    break
                else:
                    tag, msg = Server._parser(await ws.recv())
                    if msg == "#LISTDEVICES":
                        t = datetime.datetime.now()
                        path = f'D:\\Repos\\CyberController\\data\\list_device_{t.year}_{t.month}_{t.day}_{t.hour}_{t.minute}_{t.second}_{t.microsecond}.dat'
                        await ws.send(json.dumps(lib.features.scan_network(path)))
                        id = self._db.getUserID(i.username, i.password)
                        self._db.insertHistory("LISTDEVICE", path, id)
                    elif msg == "#GETPROFILE":
                        result = [i.username, self._db.getUserInfos(i.username, i.password), self._db.getHistory(
                            i.username, i.password), i.ws.remote_address]
                        result = json.dumps(result)
                        await ws.send(result)
                    elif msg == "#CLEARHISTORY":
                        self._db.clearHistory()
                        await ws.send("#ALLOW")
                    elif msg == "#EXIT":
                        self._clients.remove(i)
                        await ws.close()
                        break
                    elif msg == "#GETTASK":
                        result = json.dumps(self._db.getTasks())
                        await ws.send(result)
                    elif msg == "#INSERTTASK":
                        title = tag[1].strip()
                        description = tag[2].strip()
                        self._db.insertTask(
                            title, description, i.username, i.password)
                    elif msg == "#DELTASK":
                        title = tag[1].strip()
                        description = tag[2].strip()
                        self._db.deleteTask(
                            title, description, i.username, i.password)

        except Exception as e:
            print("Error occured at connectedClient as", e)
