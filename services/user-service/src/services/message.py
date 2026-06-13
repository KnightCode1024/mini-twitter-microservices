from fastapi import HTTPException, status

from core.uow import UnitOfWork
from repositories import MessageRepositoryI
from schemas.message import MessageCreate, MessageUpdate, MessageResponse


class MessageService:
    def __init__(
        self,
        uow: UnitOfWork,
        message_repository: MessageRepositoryI,
    ):
        self.uow = uow
        self.message_repository = message_repository

    async def create_msg(self, msg_data: MessageCreate) -> MessageResponse:
        ban_words = ["хуй", "жопа", "бля", "сука"]
        if len([1 for word in ban_words if word in msg_data.content]) > 1:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Content contain ban words: {ban_words}",
            )

        async with self.uow:
            message = await self.message_repository.create(msg_data)
            return MessageResponse(id=message.id, content=message.content)

    async def get_msg(self, msg_id: int) -> MessageResponse:
        msg = await self.message_repository.get(msg_id)
        if not msg:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Message not found.",
            )
        return MessageResponse(
            id=msg.id,
            content=msg.content,
        )

    async def get_all_msgs(self):
        messages = await self.message_repository.get_all()
        if not messages:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Messages not found.",
            )
        return messages

    async def update_msg(self, msg_id: int, msg_data: MessageUpdate):
        message = await self.message_repository.get(msg_id)
        if not message:
            raise HTTPException(
                status_code=status.H404,
                detail="Messages not found.",
            )
        async with self.uow:
            updated_msg = await self.message_repository.update(
                msg_id,
                msg_data,
            )
            return updated_msg

    async def delete_msg(self, msg_id: int) -> bool:
        message = await self.message_repository.get(msg_id)
        if not message:
            raise HTTPException(
                status_code=status.H404,
                detail="Messages not found.",
            )
        async with self.uow:
            delete_succses = await self.message_repository.delete(msg_id)
            return delete_succses
