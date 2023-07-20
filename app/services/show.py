from app.models import TvShow


class ShowCrud:
    async def add_show(self, show: TvShow):
        ...

    async def delete_show(self, title: str) -> bool:
        ...

    async def get_show_by_title(self, title):
        ...

    async def get_shows(self):
        ...

    async def update_show(self, show: TvShow):
        ...
