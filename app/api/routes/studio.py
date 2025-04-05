from fastapi import APIRouter
from app.models import Studio

router = APIRouter(
    prefix="/studio",
    tags=["studio"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get():
    return {"data": ["some studio"]}
