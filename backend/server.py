from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from typing import List, Dict
from fastapi.templating import Jinja2Templates
app = FastAPI()

# Хранение активных соединений и комнат
rooms: Dict[str, List[WebSocket]] = {}
#TODO: сделать невозможным поключение юзер без jwt
class SignalManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket, room_name: str):
        await websocket.accept()
        if room_name not in rooms:
            rooms[room_name] = []
        rooms[room_name].append(websocket)
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket, room_name: str):
        rooms[room_name].remove(websocket)
        if not rooms[room_name]:
            del rooms[room_name]

    async def broadcast(self, message, room_name: str, exclude: WebSocket):
        for connection in rooms.get(room_name, []):
            if connection is exclude:
                continue
            await connection.send_json(message)
            # await connection.send(message)

signal_manager = SignalManager()

# @app.websocket("/ws/join/{room_name}")
# async def websocket_endpoint(websocket: WebSocket, room_name: str):
#     await signal_manager.connect(websocket, room_name)
#     try:
#         await signal_manager.broadcast("ready", room_name)
#     except WebSocketDisconnect:
#         signal_manager.disconnect(websocket, room_name)
@app.websocket("/ws/{room_name}")
async def websocket_endpoint(websocket: WebSocket, room_name: str):
    await signal_manager.connect(websocket, room_name)
    try:
        while True:
            data = await websocket.receive_json()
            print(data)
            await signal_manager.broadcast(message=data, room_name=room_name, exclude=websocket)
    except WebSocketDisconnect:
        signal_manager.disconnect(websocket, room_name)

@app.get("/")
async def get():
    with open("test_network.html", encoding="utf-8") as f:
        return HTMLResponse(f.read())
    #return templates.TemplateResponse(request=request, name='index.html')
