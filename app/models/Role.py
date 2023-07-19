from pydantic import BaseModel, Field


class Role(BaseModel):
    title: {
        type: DataTypes.ENUM,
        values: ['actor', 'director'],
      }= Field(...)
    description: str = Field(...)
    createdAt: DataTypes.DATE = Field(...)
    updatedAt: DataTypes.DATE = Field(...)
