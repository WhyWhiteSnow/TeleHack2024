from database import Base, engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped


class Terminal(Base):
    __tablename__ = "terminals"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    password: Mapped[str | None] = Column(String)
    status: Mapped[str | None] = Column(String)


class Support(Base):
    __tablename__ = "supports"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    password: Mapped[str | None] = Column(String)
    status: Mapped[str | None] = Column(String)

Base.metadata.create_all(engine)