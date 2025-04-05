import datetime
from enum import Enum
from typing import List

from beanie import Document, Link
from pydantic import Field
from pydantic.networks import HttpUrl


class Episode(Document):
    name: str
    url: HttpUrl
    number: int
    length: int
    release_date: datetime.date
    description: str
    language: str


class User(Document):
    first_Name: str
    last_name: str
    email: str
    password: str


class Studio(Document):
    name: str


class RoleEnum(str, Enum):
    ACTOR = "actor"
    DIRECTOR = "director"


class Role(Document):
    title: RoleEnum
    description: str


class Genre(Document):
    name: str
    description: str


class GenreCreta(Genre):
    pass


class Employee(Document):
    """Employee base model"""

    first_name: str
    last_name: str
    gender: str
    birthdate: datetime.datetime = Field(default_factory=datetime.datetime.now)


class Anime(Document):
    name: str
    studio: Link[Studio]
    genre_tags: List[Link[Genre]]
    episode_count: int
    episode_list: List[Link[Episode]]
    thumbnail: HttpUrl
