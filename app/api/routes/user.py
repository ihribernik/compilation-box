from fastapi import APIRouter

from app.models import User

router = APIRouter(
    prefix="/user",
    tags=["user"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)



@router.get("/")
def get():
    return {"data": ["some user"]}
