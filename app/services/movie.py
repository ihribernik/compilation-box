from app.models import Movie


class MovieCrud:
    async def add_movie(self, movie: Movie):
        new_movie = Movie(title=movie.title, release_date=movie.release_date)
        await new_movie.create()

    async def delete_movie(self, title: str):
        row = await Movie.find_one(Movie.title == title)
        if row:
            await row.delete({})

    async def get_movie_by_title(self, title):
        return await Movie.find_one(Movie.title == title)

    @classmethod
    async def get_movies(cls):
        rows = await Movie.find_all().to_list()
        return rows

    async def update_movie(self, movie: Movie):
        row = await Movie.find_one(Movie.title == movie.title)

        if row:
            row.title = movie.title
            row.release_date = movie.release_date
            await row.save(Movie)
