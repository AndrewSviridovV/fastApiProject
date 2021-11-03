import sqlalchemy
from uuid import uuid4
from config import metadata
from sqlalchemy.dialects.postgresql import UUID, JSON

tasks = sqlalchemy.Table(
    "tasks",
    metadata,
    sqlalchemy.Column("task_uuid", UUID, primary_key=True, index=True, unique=True, default=uuid4),
    sqlalchemy.Column("description", sqlalchemy.Text),
    sqlalchemy.Column("params", JSON(True))
)
