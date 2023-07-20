from datetime import datetime

from beanie import Document
from pydantic import Field


class Movie(Document):
    title: str
    release_date: datetime = Field(default_factory=datetime.now)
