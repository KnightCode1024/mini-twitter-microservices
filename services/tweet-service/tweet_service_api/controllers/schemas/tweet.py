from uuid import UUID

from pydantic import BaseModel


class BaseTweetSchema(BaseModel):
    text: str


class CreateTweetSchema(BaseTweetSchema):
    user_id: UUID


class ReadTweetSchema(BaseTweetSchema):
    user_id: UUID
    media_id: UUID | None


class ResponseTweetSchema(ReadTweetSchema):
    pass


class UpdateTweetSchema(BaseModel):
    tweet_id: UUID
    user_id: UUID
    media_id: UUID | None
    text: str | None


class DeleteTweetSchema(BaseModel):
    tweet_id: UUID
    user_id: UUID
