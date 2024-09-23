from typing import List

from beanie import Document, Link
from pydantic import HttpUrl

from app.models.episode import Episode
from app.models.genre import Genre
from app.models.studio import Studio


class Anime(Document):
    name: str
    studio: Link[Studio]
    genre_tags: List[Link[Genre]]
    episode_count: int
    episode_list: List[Link[Episode]]
    thumbnail: HttpUrl
