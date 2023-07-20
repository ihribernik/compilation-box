from datetime import datetime

from beanie import Document
from pydantic import Field


class Season(Document):
    title: str
    description: str
    year: str
