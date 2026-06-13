from dishka import Provider, Scope, provide

from core.uow import UnitOfWork

# from repositories import IUserRepository
# from repositories.message import MessageRepository, MessageRepositoryI
# from services import UserService, MessageService
from repositories.user import IUserRepository
from repositories.message import MessageRepositoryI
from services.user import UserService
from services.message import MessageService


class ServiceProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def get_user_service(
        self,
        uow: UnitOfWork,
        user_repository: IUserRepository,
    ) -> UserService:
        return UserService(uow, user_repository)

    @provide
    def get_message_service(
        self,
        uow: UnitOfWork,
        message_repository: MessageRepositoryI,
    ) -> MessageService:
        return MessageService(uow, message_repository)
