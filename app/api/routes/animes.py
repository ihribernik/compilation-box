from fastapi import APIRouter
from app.models import Anime

router = APIRouter(
    prefix="/movie",
    tags=["movie"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get_movies():
    return Anime.find_all()


@router.get("/{movie_id}")
async def get_movie(movie_id: str):
    return await Anime.find_one({})


@router.post("/")
async def add_movie(body):
    anime = Anime({})
    await anime.save()
    return anime


@router.delete("/{movie_id}")
async def delete_movie(movie_id: str):
    anime = Anime.find()
    anime.delete()
    return True


@router.patch("/{movie_id}")
async def update_movie(movie_id: str, body: dict):
    anime = Anime.find({})
    anime.update({})
    return anime
