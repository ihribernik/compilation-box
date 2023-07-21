from fastapi import HTTPException
from app.models import Movie
from app.models.movie import MovieCreate, MovieUpdate


class MovieCrud:
    @classmethod
    async def add(cls, movie: MovieCreate):
        new_movie = Movie(
            title=movie.title,
            release_date=movie.release_date,
        )
        return await new_movie.create()

    @classmethod
    async def delete(cls, _id: str):
        movie = await Movie.get(_id)

        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")

        result = await movie.delete()
        return result.raw_result

    @classmethod
    async def get_by_id(cls, _id: str):
        movie = await Movie.get(_id)

        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")

        return movie

    @classmethod
    async def get_all(cls):
        return await Movie.find_all().to_list()

    @classmethod
    async def update(cls, _id: str, movie: MovieUpdate):
        row = await Movie.get(_id)
        if not row:
            raise HTTPException(status_code=404, detail="Movie not found")
        body_values = movie.model_dump(exclude_unset=True)
        return await row.set(body_values)
