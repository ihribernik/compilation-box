from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Body, HTTPException, status
from pydantic import BaseModel, EmailStr

from app.models import User
from app.core.security import create_access_token
from app.core.config import settings

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


class RequestBody(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


@router.post("/signIn", response_model=Token)
async def signIn(body: Annotated[RequestBody, Body()]):
    user: User | None = await User.find_one({"where": {"email": body.email}})

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
    )
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}
