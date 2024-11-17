from pydantic import BaseModel
class TerminalData(BaseModel):
    id:int
    password:str|None

class TerminalDataJWT(BaseModel):
    jwt:str

class SupportData(BaseModel):
    id:int
    password:str|None

class SupportDataJWT(BaseModel):
    jwt:str