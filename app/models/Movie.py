from pydantic import BaseModel, Field

from app.utils import PyObjectId


class Movie(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    releaseDate: DataTypes.DATE
    createdAt: DataTypes.DATE
    updatedAt: DataTypes.DATE
