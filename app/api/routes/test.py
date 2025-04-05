from fastapi import APIRouter

from app.models import Genre

router = APIRouter(
    prefix="/test",
    tags=["test"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def post():
    genre = Genre(name="some genre", description="some description")
    return await genre.save()
