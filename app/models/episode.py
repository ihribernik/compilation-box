from datetime import datetime

from beanie import Document
from pydantic import Field


class Episode(Document):
    title: str
    description: str
