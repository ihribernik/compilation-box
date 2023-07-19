from fastapi import APIRouter

router = APIRouter(
    prefix="auth",
    tags=["auth"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post("/signIn")
async def signIn():
    ...


@router.post("/refresh")
async def refreshToken():
    ...
