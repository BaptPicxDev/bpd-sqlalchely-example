import os
from fastapi import (
    UploadFile,
    FastAPI,
)
import uvicorn


from src.database import (
    create_engine,
    get_connection,
    close_connection,
)
from src.models import (
    Task,
    Base
)


def get_api() -> FastAPI:
    app = FastAPI()
    engine = create_engine()
    Base.metadata.create_all(bind=engine)
    conn = get_connection(engine=engine)

    @app.get("/")
    async def index() -> dict:
        print(Task.list_all(conn))
        return {"status_code": 200, "message": "hello world"}

    @app.post("/create_task")
    async def create_task() -> dict:
        new_task = Task(name="hep")
        conn.add(new_task)
        conn.commit()
        return {"status_code": 200, "message": f"hello world: {new_task.uuid}"}

    @app.post("/status")
    async def status(uuid: str) -> dict:
        r = Task.get_state_by_uuid(conn, uuid)
        return {"status_code": 200, "message": f"status: {r}"}

    return app


def run_wsgi(app: FastAPI) -> None:
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
    )


if __name__ == "__main__":
    app = get_api()
    run_wsgi(app)
