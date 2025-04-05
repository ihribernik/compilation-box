from fastapi import APIRouter
from app.models import Anime

router = APIRouter(
    prefix="/anime",
    tags=["anime"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_movies():
    animes = Anime.find_all(limit=100)
    animes = await animes.to_list()
    return animes


@router.get("/{movie_id}")
async def get_movie(movie_id: str):
    anime = await Anime.find_one()
    return anime


@router.post("/")
async def add_movie():
    anime = Anime({})
    await anime.save()
    return anime


@router.delete("/{movie_id}")
async def delete_movie(movie_id: str):
    anime = Anime.find()
    anime.delete()
    return True


@router.put("/{movie_id}")
async def update_movie(movie_id: str, body: dict):
    anime = Anime.find({})
    anime.update({})
    return anime
