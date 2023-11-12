from sqlalchemy import Column, Integer, String, UUID
from sqlalchemy import CheckConstraint
from sqlalchemy.ext.declarative import declarative_base


from src.utils import (
    generate_uuid,
    get_datetime_ymdhms,
)


Base = declarative_base()


class Task(Base):
    """Task."""
    __tablename__ = "task"

    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    timestamp = Column(String, nullable=False, default=get_datetime_ymdhms)
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

    @classmethod
    def update_task_status(cls, session, uuid_to_query: str, new_state: str) -> str:
        """
        Retrieve a Task using uuid.
        Then update the state.

        :param session: SQLAlchemy session
        :param uuid_to_query: UUID to query
        :return: Task state or None if not found
        """
        task = session.query(cls).filter(cls.uuid == uuid_to_query).first()
        if task.state != new_state:
            task.state = new_state
            session.commit()

    @classmethod
    def list_all_running(cls, session) -> list:
        """
        Retrieve all the Task objects which are running.

        :param session: SQLAlchemy session
        :return: all running Task
        """
        return (
            session
            .query(cls)
            .select(cls.name, cls.timestamp, cls.uuid)
            .filter(cls.state=="running")
            .all()
        )

    @classmethod
    def list_all(cls, session) -> list:
        """
        Retrieve all the Task objects.

        :param session: SQLAlchemy session
        :return: all Task
        """
        return (
            session
            .query(cls.name, cls.timestamp, cls.uuid, cls.state)
            .all()
        )

    def __repr__(self) -> str:
        return f"<Task: {self.id}>"
