from routers.dev_router import router as dev_router
from routers.user_router import router as user_router
from routers.note_service_router import router as note_service_router
from routers.root_router import root_router

__all__ = [
    "dev_router",
    "user_router",
    "note_service_router",
    "root_router",
]
