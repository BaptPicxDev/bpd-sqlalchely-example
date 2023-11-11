from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base

from src.utils import generate_uuid


Base = declarative_base()


class Task(Base):
    """Task."""
    __tablename__ = "task"

    id = Column(Integer, nullable=False, primary_key=True)
    uuid = Column(String, nullable=False)
    name = Column(String, nullable=False)
    state = Column(String, nullable=False, default="created")

    def __repr__(self) -> str:
        return f"<Task: {self.id}>"
