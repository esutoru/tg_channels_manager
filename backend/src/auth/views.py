from fastapi import APIRouter, Response

from backend.src.auth.schemas import LoginData
from backend.src.auth.security import generate_jwt_token
from backend.src.config import settings

router = APIRouter()


@router.post("/login")
async def login(user_data: LoginData, response: Response) -> dict:
    # TODO: Get user and check password
    user_id = 1

    response.set_cookie(
        "Authorization",
        value=f"Bearer {generate_jwt_token({'user_id': user_id})}",
        httponly=True,
        max_age=settings.JWT_AUTH_TOKEN_EXPIRY,
        secure=settings.DOMAIN_HTTPS,
    )

    return {"success": True}


@router.post("/logout")
async def logout(response: Response) -> dict:
    response.set_cookie("Authorization", max_age=0)
    return {"success": True}
