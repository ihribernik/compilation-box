from fastapi import APIRouter
from app.services.movie import MovieCrud

router = APIRouter(
    prefix="/movie",
    tags=["movie"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def getMovies():
    return await MovieCrud.get_movies()


@router.get("/{id}")
async def getMovie(id: int):
    ...


@router.post("/")
async def addMovie():
    ...


@router.delete("/{id}")
async def deleteMovie(id: int):
    ...


@router.patch("/{id}")
async def updateMovie(id: int):
    ...
