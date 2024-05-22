from websockets.sync.client import connect

def hello():
    # with connect("wss://echo.websocket.org") as websocket:
    with connect("ws://localhost:5000") as websocket:
        websocket.send("Hello world!")
        message = websocket.recv()
        print(f"Received: {message}")

hello()