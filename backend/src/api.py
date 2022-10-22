from backend.src.example.views import router as example_router
from fastapi import APIRouter

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(example_router, prefix="/example", tags=["Example"])
