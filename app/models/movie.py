from datetime import datetime

from beanie import Document
from pydantic import BaseModel, Field


class Movie(Document):
    title: str
    release_date: datetime = Field(default_factory=datetime.now)


class MovieCreate(BaseModel):
    title: str
    release_date: datetime


class MovieUpdate(BaseModel):
    title: str | None = None
    release_date: datetime | None = None
