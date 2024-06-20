import asyncio
import websockets
import threading
import time

class Server:
    def __init__(self, port):
        self._port = port
        self._clients = []

    def run(self):
        start_server = websockets.serve(
            self.__clientHandler, "localhost", self._port)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

    async def __clientHandler(self, socket):
        print(f"Client connected from {socket.remote_address}")
        self._clients.append(socket)

        try:
            while True:
                message = await socket.recv()

                if message.lower() == "exit":
                    print(f"Connection closed {socket.remote_address}")
                    self._clients.remove(socket)
                    await socket.close()
                    break

                print(
                    f"Recieved Message {message} from {socket.remote_address}")

                await socket.send(f"Reversed: {message[::-1]}")
        except websockets.ConnectionClosed:
            self._clients.remove(socket)
            print(f"Client from {socket.remote_address} disconnected")
        except Exception as e:
            print(f"Error occured {e} from {socket.address}")
        finally:
            if socket in self._clients:
                self._clients.remove(socket)
                await socket.close()
                print(f"Connection closed {socket.remote_address}")

    def PrintClients(self):
        print(self._clients)
        for i in self._clients:
            print(f"{i}:{i.remote_address}")


if __name__ == "__main__":
    obj1 = Server(9999)
    obj1.run()
    
    print("Server started . . .")
    
    while True:
        obj1.PrintClients()
        time.sleep(2)