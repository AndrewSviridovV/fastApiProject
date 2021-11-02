import sqlalchemy
from sqlalchemy import Column, String
from config import metadata
from sqlalchemy.dialects.postgresql import UUID, JSON

# from config import Base


tasks = sqlalchemy.Table(
    "tasks",
    metadata,
    sqlalchemy.Column("task_uuid", UUID(as_uuid=True), primary_key=True, index=True, unique=True),
    sqlalchemy.Column("description", sqlalchemy.Text),
    sqlalchemy.Column("params", JSON(True))
)

# class Task(Base):

#   __tablename__ = "tasks"

#    task_uuid = Column(UUID(as_uuid=True), primary_key=True, index=True, unique=True)
#   description = Column(String(100))
#    params = Column(JSON(True))
