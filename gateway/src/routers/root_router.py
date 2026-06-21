from fastapi import APIRouter

from routers import (
    dev_router,
    user_router,
    note_service_router
)

root_router = APIRouter(prefix="/api/v1")

routers = [
    dev_router,
    user_router,
    note_service_router,
]

for router in routers:
    root_router.include_router(router)
