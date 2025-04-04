from fastapi import APIRouter

router = APIRouter(
    prefix="/show",
    tags=["show"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/{id}")
async def getSerie(id: int):
    ...
