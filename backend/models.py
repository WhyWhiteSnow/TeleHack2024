from database import Base
from sqlalchemy import Column,Integer,String
class Terminal(Base):
    __tablename__ = 'terminals'
    id = Column(Integer, primary_key=True, index=True)
    password = Column(String)
    status=Column(String)
class Support(Base):
    __tablename__ = 'supports'
    id = Column(Integer, primary_key=True, index=True)
    password = Column(String)
    status=Column(String)