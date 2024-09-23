import asyncio
import json
import logging
import time
from pprint import pprint
from typing import Dict, List
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from app.models import Anime, Genre
from app.settings.database import init

logger = logging.getLogger(__name__)


class NotFoundException(Exception):
    """Not Found webpage on fetch"""


class Command:
    """scrap page command for django cli"""

    file_location: str
    url_location: str

    def __init__(self, file_location: str, url_location: str) -> None:
        self.file_location = file_location
        self.url_location = url_location

    @staticmethod
    def process_page(elements: list, url_location: str) -> list:
        """
        process the current page and return a dict with page an anime list
        """

        anime_list = [
            {
                "href": urljoin(url_location, element.get("href")),
                "name": element.img["alt"],
            }
            for element in elements
        ]

        return anime_list

    @staticmethod
    def get_tags(page: BeautifulSoup, page_structure: dict):
        """get the tags from the page"""

        selected_tags = page.select(page_structure["tags"])
        tags = [tag.text for tag in selected_tags]

        return tags

    @staticmethod
    def fetch_page(url_location: str, page_index: int) -> BeautifulSoup:
        """get the page by url or throw an exception"""

        response = requests.get(
            url=f"{url_location}/page/{page_index}",
            timeout=500,
        )

        if response.status_code != 200:
            raise NotFoundException(
                f"Unable to Fetch page {url_location=} in index {page_index=}"
            )

        page = response.content
        soup = BeautifulSoup(page, "html.parser")
        return soup

    @staticmethod
    def parse_titles_page(page: BeautifulSoup, page_structure: dict):
        """parse the current page with the page_structure"""

        elements = page.select(page_structure["elements"])
        current_page = page.select(page_structure["current_page"])[0].text
        last_page = page.select(page_structure["last_page"])[-1].text

        return elements, current_page, last_page

    async def process_url(self):
        """handle entrypoint"""
        await self.process_url()
        base_url = "http://" + self.url_location
        page_structure = self.get_page_structure(self.file_location)
        page = self.fetch_page(base_url, page_index=1)
        elements, current_page, last_page = self.parse_titles_page(
            page,
            page_structure,
        )
        tags = self.get_tags(page, page_structure)

        for tag in tags:
            genre = Genre(name=tag, description="")
            await genre.create()

        anime_list = self.get_anime_list(
            base_url, page_structure, elements, current_page, last_page
        )

        for anime in anime_list:
            print(anime)

    def get_anime_list(
        self, base_url, page_structure, elements, current_page, last_page
    ):
        anime_list = []
        for page_index in range(int(last_page)):
            if page_index == 0:
                anime_page = self.process_page(elements, base_url)
                anime_list.append(anime_page)
                continue

            page = self.fetch_page(base_url, page_index + 1)

            elements, _current_page, last_page = self.parse_titles_page(
                page, page_structure
            )

            anime_page = self.process_page(elements, base_url)
            anime_list.append(anime_page)
            logger.info(f"parsed page {page_index}. now sleeping 10 seconds..")
            time.sleep(10)
        return anime_list

    def get_page_structure(self, file_path: str) -> dict:
        """get the page structure from a json file"""

        with open(file=file_path, mode="r", encoding="utf-8") as file:
            page_structure = json.loads(file.read())
        return page_structure

    async def add_animes(self, animes):

        for anime in animes:
            pprint(anime)
            for anime_page in anime["animes"]:
                genre = anime["genre"]
                genre_obj = Genre.objects.get_or_create(name=genre)
                anime_page["genre"] = genre_obj[0]
                anime = Anime(**anime_page)
                await anime.create()

    def get_studios(self, page: BeautifulSoup, page_structure: dict):
        """get the studios from the page"""

        selected_studios = page.select(page_structure["studios"])
        studios = [studio.text for studio in selected_studios]

        return studios


async def main():
    await init()
    file_location = ""
    url_location = ""
    command = Command(file_location, url_location)
    await command.process_url()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
