# from dishka import make_async_container
# from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

# from tweet_service_api.controllers import root_controller
from tweet_service_api.controllers.http import root_controller
# from book_club.config import Config
# from book_club.controllers.http import book_router
# from book_club.infrastructure.resources.broker import new_broker
# from book_club.ioc import AppProvider

# config = Config()
# container = make_async_container(AppProvider(), context={Config: config})


def get_fastapi_app() -> FastAPI:
    fastapi_app = FastAPI()
    fastapi_app.include_router(root_controller)

    # setup_dishka(container, fastapi_app)

    return fastapi_app


def get_app():
    fastapi_app = get_fastapi_app()
    return fastapi_app
