from fastapi import Request
from fastapi.security.utils import get_authorization_scheme_param

from backend.src.auth.security import get_jwt_token_params


async def get_current_user(request: Request) -> dict | None:
    authorization_header_value = request.cookies.get("Authorization")
    if not authorization_header_value:
        return None

    scheme, token = get_authorization_scheme_param(authorization_header_value)
    if not token or scheme.lower() != "bearer":
        return None

    if params := get_jwt_token_params(token):
        # TODO: Try to return user object there
        return {"user_id": params["user_id"]}

    return None
