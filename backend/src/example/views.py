from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root() -> dict:
    return {"message": "Hello World!"}


@router.get("/hello/{name}")
async def say_hello(name: str) -> dict:
    return {"message": f"Hello {name}"}
