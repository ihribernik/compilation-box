from datetime import datetime
from enum import Enum

from bson import DatetimeMS, ObjectId
from pydantic import BaseModel, Field

from app.utils import PyObjectId


class BasePyObjectIdModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")


class EmployeeModel(BasePyObjectIdModel):
    """Employee base model"""

    firstName: str
    lastName: str
    gender: str
    birthdate: datetime

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "firstName": "",
                "lastName": "",
                "gender": "",
                "birthdate": "",
                "createdAt": "",
                "updatedAt": "",
            }
        }


class Episode(BasePyObjectIdModel):
    title: str
    description: str
    createdAt: DatetimeMS
    updatedAt: DatetimeMS


class Movie(BasePyObjectIdModel):
    title: str
    releaseDate: DatetimeMS
    createdAt: DatetimeMS
    updatedAt: DatetimeMS


class RoleEnum(str, Enum):
    actor = "actor"
    director = "director"


class Role(BasePyObjectIdModel):
    title: RoleEnum
    description: str
    createdAt: DatetimeMS
    updatedAt: DatetimeMS


class Season(BasePyObjectIdModel):
    title: str
    description: str
    year: str
    createdAt: DatetimeMS
    updatedAt: DatetimeMS


class TvShow(BasePyObjectIdModel):
    title: str
    description: str
    duration: int
    createdAt: DatetimeMS
    updatedAt: DatetimeMS


class User(BasePyObjectIdModel):
    firstName: str
    lastName: str
    email: str
    password: str
    createdAt: DatetimeMS
    updatedAt: DatetimeMS
