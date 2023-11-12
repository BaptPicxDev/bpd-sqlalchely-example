from sqlalchemy import Column, Integer, String, UUID
from sqlalchemy import CheckConstraint
from sqlalchemy.ext.declarative import declarative_base


from src.utils import generate_uuid


Base = declarative_base()


class Task(Base):
    """Task."""
    __tablename__ = "task"

    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String, nullable=False)
    uuid = Column(UUID, nullable=False, unique=True, default=generate_uuid)
    state = Column(String, CheckConstraint("state IN ('created', 'running', 'finished')"), nullable=False, default="created")

    def __repr__(self) -> str:
        return f"<Task: {self.id}>"
