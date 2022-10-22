from fastapi import FastAPI

from backend.src.api import api_router
from backend.src.config import settings

app = FastAPI(
    title="Telegram Channels Manager's API",
    description=(
        "Welcome to Telegram Channels API documentation! Here you will able to discover "
        "all of the ways you can interact with the Telegram Channels API."
    ),
    debug=settings.DEBUG,
)


app.include_router(api_router)
