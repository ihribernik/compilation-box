from fastapi import APIRouter
from app.services.anime import AnimeCrud

# from app.models.anime import MovieCreate, MovieUpdate

router = APIRouter(
    prefix="/movie",
    tags=["movie"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def getMovies():
    return await AnimeCrud.get()


@router.get("/{movie_id}")
async def getMovie(movie_id: str):
    return await AnimeCrud.get()


@router.post("/")
async def addMovie(body):
    return await AnimeCrud.add()


@router.delete("/{movie_id}")
async def deleteMovie(movie_id: str):
    return await AnimeCrud.delete("")


@router.patch("/{movie_id}")
async def updateMovie(movie_id: str, body: dict):
    return await AnimeCrud.update()
