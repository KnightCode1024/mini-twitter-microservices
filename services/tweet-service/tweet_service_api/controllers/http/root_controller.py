from fastapi import APIRouter

from tweet_service_api.controllers.http.tweet_controller import controller as tweet_controller

root_controller = APIRouter(prefix="/api/v1")

controllers = [
    tweet_controller
]

for controller in controllers:
    root_controller.include_router(controller)
