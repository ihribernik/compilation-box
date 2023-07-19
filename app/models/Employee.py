from bson import ObjectId
from pydantic import BaseModel, Field

from app.utils import PyObjectId
from datetime import datetime


class EmployeeModel(BaseModel):
    """Employee base model"""

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    firstName: str = Field(...)
    lastName: str = Field(...)
    gender: str = Field(...)
    birthdate: datetime = Field(...)

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
