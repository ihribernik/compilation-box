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
    return await AnimeCrud.get_all()


@router.get("/{movie_id}")
async def getMovie(movie_id: str):
    return await AnimeCrud.get_by_id(_id=movie_id)


@router.post("/")
async def addMovie(body: MovieCreate):
    return await AnimeCrud.add(movie=body)


@router.delete("/{movie_id}")
async def deleteMovie(movie_id: str):
    return await AnimeCrud.delete(_id=movie_id)


@router.patch("/{movie_id}")
async def updateMovie(movie_id: str, body: MovieUpdate):
    return await AnimeCrud.update(_id=movie_id, movie=body)
