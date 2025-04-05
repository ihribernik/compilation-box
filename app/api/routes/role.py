from fastapi import APIRouter
from app.models import Role

router = APIRouter(
    prefix="/role",
    tags=["role"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get():
    return {"data": ["some role"]}
