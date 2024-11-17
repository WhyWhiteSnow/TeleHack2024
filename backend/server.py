from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends, HTTPException,status
from fastapi.responses import HTMLResponse
from typing import List, Dict
# from fastapi.templating import Jinja2Templates
# from fastapi.security import OAuth2PasswordBearer

from database import get_db
from sqlalchemy.orm import Session

from passlib.context import CryptContext
# import os
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt
from models import Terminal,Support
from schemas import TerminalData,TerminalDataJWT, SupportData,SupportDataJWT
from jwt_settings import *

app = FastAPI()
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
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


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
   
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm='HS256')
    
    return encoded_jwt

@app.get("/terminals")
def get_users(db:Session = Depends(get_db)):
    terminals = db.query(Terminal).all()
    return [{'id':terminal.id, 'password':terminal.password,'status':terminal.status} for terminal in terminals]

@app.get('/getrooms')
def get_rooms(supportdata:SupportDataJWT,db:Session = Depends(get_db)):
    if check_support_jwt(supportdata.jwt, db):
        return {"rooms":rooms}
    return {"details":"wrong jwt"}

@app.get("/autoriseTerminal/")
def get_users(terminaldata:TerminalData, db:Session = Depends(get_db)):
    try:
        terminal = db.query(Terminal).get(terminaldata.id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверные учетные данные",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if terminal.password == terminaldata.password:
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"id": terminal.id, "password":terminal.password}, expires_delta=access_token_expires)
        # print(access_token)
        return {"jwt":access_token}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверные учетные данные",
            headers={"WWW-Authenticate": "Bearer"},
        )

@app.get("/autoriseSupport/")
def get_users(supportdata:SupportData, db:Session = Depends(get_db)):
    try:
        support = db.query(Support).get(supportdata.id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверные учетные данные",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if support.password == supportdata.password:
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"id": support.id, "password":support.password}, expires_delta=access_token_expires)
        # print(access_token)
        return {"jwt":access_token}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверные учетные данные",
            headers={"WWW-Authenticate": "Bearer"},
        )

# @app.get("/checkTerminalJWT/")
# def check_terminal_jwt(terminaldata:TerminalDataJWT, db:Session = Depends(get_db)):
def check_terminal_jwt(terminalJWT, db):
    try:
        decoded_jwt = jwt.decode(terminalJWT, SECRET_KEY, algorithms='HS256')
        terminal = db.query(Terminal).get(decoded_jwt["id"])
        if decoded_jwt['exp']!=0:
            # return {"detail":'ok'}
            return True
        return False
    except Exception as e:
        return False
# @app.get("/checkSupportJWT/")
# def check_support_jwt(supportdata:SupportDataJWT, db:Session = Depends(get_db)):
def check_support_jwt(supportJWT,db):
    try:
        decoded_jwt = jwt.decode(supportJWT, SECRET_KEY, algorithms='HS256')
        support = db.query(Support).get(decoded_jwt["id"])
        if decoded_jwt['exp']!=0:
            return True
        return False
    except Exception as e:
        # raise HTTPException(
        #     status_code=status.HTTP_401_UNAUTHORIZED,
        #     detail="Неверный jwt токен",
        #     headers={"WWW-Authenticate": "Bearer"},
        # )
        return False