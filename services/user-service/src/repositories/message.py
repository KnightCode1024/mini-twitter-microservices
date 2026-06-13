from typing import Protocol

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from models import Message
from schemas.message import MessageCreate, MessageUpdate


class MessageRepositoryI(Protocol):
    async def get(self, msg_id: int) -> Message | None: ...

    async def get_all(
        self, offset: int = 0, limit: int = 20
    ) -> list[Message] | None: ...

    async def create(self, msg_data: MessageCreate) -> Message: ...

    async def update(
        self,
        msg_id: int,
        msg_data: MessageUpdate,
    ) -> Message | None: ...

    async def delete(self, msg_id: int) -> bool: ...


class MessageRepository(MessageRepositoryI):
    def __init__(
        self,
        session: AsyncSession,
    ):
        self.session = session

    async def get(self, msg_id: int) -> Message:
        query = select(Message).where(Message.id == msg_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_all(
        self,
        offset: int = 0,
        limit: int = 20,
    ) -> list[Message]:
        query = select(Message).offset(offset).limit(limit)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def create(self, msg_data: MessageCreate) -> Message:
        message = Message(**msg_data.model_dump())
        self.session.add(message)
        await self.session.flush()
        return message

    async def update(
        self,
        msg_id: int,
        msg_data: MessageUpdate,
    ) -> Message | None:
        messaage = await self.get(msg_id)
        if not messaage:
            return None
        updated_data = msg_data.model_dump(exclude_unset=True)
        for field, value in updated_data.items():
            setattr(messaage, field, value)
        self.session.add(messaage)
        return messaage

    async def delete(self, msg_id: int) -> bool:
        message = await self.session.get(Message, msg_id)
        if not message:
            return False

        stmt = delete(Message).where(Message.id == msg_id)
        await self.session.execute(stmt)
        await self.session.flush()
        return True
