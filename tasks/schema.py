from uuid import UUID, uuid4

from pydantic import BaseModel, Field, Json


class Task(BaseModel):
    task_uuid: UUID = Field(default_factory=uuid4)
    description: str
    params: Json

    class Config:
        orm_mode = True
