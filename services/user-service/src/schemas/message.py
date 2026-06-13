from pydantic import BaseModel, Field


class BaseMessage(BaseModel):
    id: int
    content: str


class MessageCreate(BaseModel):
    content: str = Field(..., min_length=10, max_length=100)


class MessageUpdate(BaseModel):
    content: str = Field(..., min_length=10, max_length=100)


class MessageResponse(BaseMessage):
    pass
