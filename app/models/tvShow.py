from datetime import datetime

from beanie import Document
from pydantic import Field


class TvShow(Document):
    title: str
    description: str
    duration: int
