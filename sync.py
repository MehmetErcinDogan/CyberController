import websockets.sync.server
import threading
import time

def echo(ws):
    print("Client connected")
    try:
        while True:
            message = ws.recv()  # Receive a message from the client
            if message is None:
                break  # Client disconnected
            print(f"Received message: {message}")
            ws.send(f"Echo: {message}")  # Echo the message back to the client
    finally:
        ws.close()
        print("Client disconnected")

# Start the WebSocket server
server = websockets.sync.server.serve(echo, "localhost", 8765)

print("Server started on ws://localhost:8765")
time.sleep(2)

def x():
    for i in range(10**10):
        print("i")

def y():
    for i in range(10**10):
        print("j")

threading.Thread(target=server.serve_forever).start()
threading.Thread(target=x).start()
threading.Thread(target=y).start()