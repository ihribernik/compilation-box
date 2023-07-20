from typing import Annotated

import bcrypt
from fastapi import APIRouter, Body
from models.models import User
from pydantic import BaseModel, EmailStr
from utils.security import create_token

from app.utils.constants import (
    LOGIN_ERROR,
)

router = APIRouter(
    prefix="auth",
    tags=["auth"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


class RequestBody(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    token: str


class RefreshTokenResponse(TokenResponse):
    refresh_token: str


@router.post("/signIn")
async def signIn(body: Annotated[RequestBody, Body()]) -> RefreshTokenResponse:
    try:
        user: User = await User.findOne({"where": {"email": body.email}})

        if not user:
            return res.status(401).json({"error": LOGIN_ERROR})

        bytes = body.password.encode("utf-8")
        salt = bcrypt.gensalt()
        encripted_password = bcrypt.hashpw(bytes, salt)

        passwordIsValid = bcrypt.checkpw(encripted_password, user.password)

        if not passwordIsValid:
            return res.status(401).json({"error": LOGIN_ERROR})

        userCred = {
            "firstName": user.firstName,
            "lastName": user.lastName,
            "email": user.email,
            "password": user.password,
        }

        # token = encodeToken(userCred, EXPIRE_TOKEN, SECRET_TOKEN)
        # refreshToken = encodeToken(
        #     userCred,
        #     EXPIRE_REFRESH_TOKEN,
        #     SECRET_REFRESH_TOKEN,
        # )
        token = create_token()
        refreshToken = create_token()

        return res.status(200).json({token, refreshToken})
    except Exception as exc:
        return res.status(500).json({"message": exc.message})


@router.post("/refresh")
async def refreshToken(body: Annotated[RequestBody, Body()]) -> TokenResponse:
    try:
        token = create_token()
        return res.status(200).json({token})
    except Exception as exc:
        return res.status(500).json({"message": exc})
