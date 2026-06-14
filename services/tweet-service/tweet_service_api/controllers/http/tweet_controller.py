from fastapi import APIRouter
from dishka.integrations.fastapi import FromDishka, DishkaRoute

from tweet_service_api.controllers.schemas.tweet import (
    CreateTweetSchema, 
    ReadTweetSchema, 
    UpdateTweetSchema, 
    DeleteTweetSchema,
    ResponseTweetSchema,
)

controller = APIRouter(
    prefix="/tweet", 
    tags=["Tweet"], 
    route_class=DishkaRoute,
    )

@controller.post("/", response_model=ResponseTweetSchema)
def create_tweet(
    tweet_data: CreateTweetSchema,
):
    pass

@controller.get("/", response_model=list[ResponseTweetSchema])
def read_tweets(
    tweet_data: ReadTweetSchema,
    offset: int = 0,
    limit: int = 20,
):
    pass

@controller.patch("/", response_model=ResponseTweetSchema)
def update_tweet(
    tweet_data: UpdateTweetSchema,
):
    pass

@controller.delete("/")
def delete_tweet(
    tweet_data: DeleteTweetSchema,
):
    pass
