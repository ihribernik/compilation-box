from pydantic import BaseModel, Field
from bson import DatetimeMS

from app.utils import PyObjectId


class Episode(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    description: str = Field(...)
    createdAt: DatetimeMS = Field(...)
    updatedAt: DatetimeMS = Field(...)
