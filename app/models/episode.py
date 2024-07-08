import datetime

from beanie import Document
from pydantic import Field, HttpUrl


class Episode(Document):
    name: str
    url: HttpUrl
    number: int
    length: int
    release_date: datetime.date
    description: str
    language: str
