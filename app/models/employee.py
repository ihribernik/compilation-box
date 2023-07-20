from datetime import datetime

from beanie import Document
from pydantic import Field


class Employee(Document):
    """Employee base model"""

    first_name: str
    last_name: str
    gender: str
    birthdate: datetime = Field(default_factory=datetime.now)
