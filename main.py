from config import engine
from config import metadata
from config import app
import uvicorn


from tasks.route import task_route

app.include_router(task_route, prefix="/tasks", tags=["task"])




if __name__ == '__main__':
    metadata.create_all(engine)
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
