from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from core.uow import UnitOfWork
from repositories import (
    IUserRepository,
    UserRepository,
    # MessageRepository,
    # MessageRepositoryI,
)
from repositories.message import MessageRepository, MessageRepositoryI


class RepositoryProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def get_user_repository(self, session: AsyncSession) -> IUserRepository:
        return UserRepository(session)

    @provide
    def get_message_repository(
        self,
        session: AsyncSession,
    ) -> MessageRepositoryI:
        return MessageRepository(session)

    @provide
    def get_unit_of_work(self, session: AsyncSession) -> UnitOfWork:
        return UnitOfWork(session)
