from fastapi import APIRouter

# from app.models.anime import MovieCreate, MovieUpdate
# from app.services.movie import MovieCrud

router = APIRouter(
    prefix="/movie",
    tags=["movie"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def getMovies():
    return await MovieCrud.get_all()


@router.get("/{movie_id}")
async def getMovie(movie_id: str):
    return await MovieCrud.get_by_id(_id=movie_id)


@router.post("/")
async def addMovie(body: MovieCreate):
    return await MovieCrud.add(movie=body)


@router.delete("/{movie_id}")
async def deleteMovie(movie_id: str):
    return await MovieCrud.delete(_id=movie_id)


@router.patch("/{movie_id}")
async def updateMovie(movie_id: str, body: MovieUpdate):
    return await MovieCrud.update(_id=movie_id, movie=body)
