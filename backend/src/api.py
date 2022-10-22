from fastapi import APIRouter

from backend.src.example.views import router as example_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(example_router, prefix="/example", tags=["Example"])
