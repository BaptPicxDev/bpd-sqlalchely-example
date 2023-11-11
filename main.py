import argparse

from src.database import *
from src.models import *

parser = argparse.ArgumentParser(
    prog='PoetryTest',
    description='This is a poetry tutorial',
)
parser.add_argument(
    "-d",
    "--dev",
    action="store_true",
    help='Run the progam in development mode.',
)


if __name__ == "__main__":
    args = parser.parse_args()
    if args.dev:
        print("Dev mode.")
    else:
        from src.database import (
            create_engine,
            get_connection,
            close_connection,
        )
        from src.models import Task
        engine = create_engine()
        Base.metadata.create_all(bind=engine)
        conn = get_connection(engine=engine)
        conn.add(
            Task(uuid="a", name="b", state="c")
        )
        conn.commit()
        close_connection(conn=conn)
        print("Production mode.")
        remove_database()
