from fastapi import APIRouter
from app.core.logger import logger
from app.models import Genre

router = APIRouter(
    prefix="/genre",
    tags=["genre"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get():
    genres = Genre.find_all()
    results = await genres.to_list()
    logger.warning({"data": results})
    return {"data": results}
