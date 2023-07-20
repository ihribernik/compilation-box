from beanie import Document

from app.models.roleEnum import RoleEnum


class Role(Document):
    title: RoleEnum
    description: str
