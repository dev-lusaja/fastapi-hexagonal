from fastapi import FastAPI
from app.infrastructure.container import Container
from app.infrastructure.handlers import Handlers


def create_app():
    fast_api = FastAPI()
    fast_api.container = Container()
    for handler in Handlers.iterator():
        fast_api.include_router(handler.router)
    return fast_api
