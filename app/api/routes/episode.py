from fastapi import APIRouter
from app.models import Episode

router = APIRouter(
    prefix="/episode",
    tags=["episode"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get():
    return {"data": ["some episode"]}
