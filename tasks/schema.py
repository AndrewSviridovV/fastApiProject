
from pydantic import BaseModel,  Json, UUID4


class TaskItem(BaseModel):
    description: str
    params: Json


class Task(TaskItem):
    task_uuid: UUID4
