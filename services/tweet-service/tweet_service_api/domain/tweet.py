from uuid import UUID
from dataclasses import dataclass


@dataclass(slots=True)
class TweetDM:
    tweet_id: UUID
    user_id: UUID
    media_id: UUID
    text: str
