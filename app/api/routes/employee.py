from fastapi import APIRouter
from app.models import Employee

router = APIRouter(
    prefix="/employee",
    tags=["employee"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get():
    return {"data": ["some employee"]}
