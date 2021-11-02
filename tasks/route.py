from fastapi import APIRouter
from typing import List

from sqlalchemy.dialects.postgresql import UUID

from config import database


from model import tasks
from schema import Task

task_route = APIRouter()


@task_route.get("/tasks", response_model=List[Task], status_code=200)
async def all_tasks():
    query = tasks.select()
    all_tasks = await database.fetch_all(query)
    if tasks is None:
        return {"message": " No post found!"}
    else:
        return all_tasks

@task_route.post("/add", response_model=Task, status_code=201)
async def create(task: tasks):
    query = tasks.insert().values(task_uuid=task.task_uuid, description=task.description, params=task.params)
    last_record = await database.execute(query=query)
    return {**task.dict(), "uuid": last_record}


@task_route.put("/tasks/{uuid}", response_model=Task)
async def update(uuid:UUID, task: Task):
    query = tasks.update().where(tasks.c.uuid == uuid).values(task_uuid=task.task_uuid, description=task.description,
                                                              params=task.params)
    last_record = await database.execute(query=query)
    return {**task.dict(), "uuid": last_record}

