import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker
# from src.models import(
#     Task,
# )

def create_engine(file_path="database.db") -> sqlalchemy.engine.base.Engine:
    """Create engine"""
    print(f"Creating engine. Connecting with {file_path}.")
    return sqlalchemy.create_engine(f"sqlite:///{file_path}", echo=False)


def get_connection(engine: sqlalchemy.engine.base.Engine) -> sqlalchemy.engine.base.Connection:
    """Create Engine connection."""
    print(f"Creating connector.")
    Session = sessionmaker(bind=engine)
    return Session()


def close_connection(conn: sqlalchemy.engine.base.Connection) -> None:
    """Close Engine connection."""
    print(f"Closing connector.")
    conn.close()


def remove_database(file_path="database.db") -> None:
    """Remove the database."""
    if not os.path.exists(file_path):
        raise FileNotFoundError()
    print(f"Removing database: {file_path}.")
    os.remove(file_path)


if __name__ == "__main__":
    engine = create_engine()
    conn = get_connection(engine=engine)
    # conn.add(
    #     Task()
    # )
    # conn.commit()
    close_connection(conn=conn)