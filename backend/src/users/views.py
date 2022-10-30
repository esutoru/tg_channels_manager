from fastapi import APIRouter, Depends

from backend.src.users.dependencies import get_current_user

router = APIRouter()


@router.get("/me")
async def get_current_user_data(user: dict = Depends(get_current_user)) -> dict:
    # TODO: Serialize user data
    return user
