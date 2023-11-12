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
    uuid = Column(String, nullable=False, unique=True, default=generate_uuid)
    state = Column(String, CheckConstraint("state IN ('created', 'running', 'finished')"), nullable=False, default="created")

    @classmethod
    def get_state_by_uuid(cls, session, uuid_to_query: str) -> str:
        """
        Retrieve the state of a Task based on the UUID.

        :param session: SQLAlchemy session
        :param uuid_to_query: UUID to query
        :return: Task state or None if not found
        """
        task = session.query(cls).filter(cls.uuid == uuid_to_query).first()
        return task.state if task else None

    def __repr__(self) -> str:
        return f"<Task: {self.id}>"
