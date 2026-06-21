from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter, Request, status, Response
import httpx

from entrypoint.config import Config


router = APIRouter(
    prefix="/note-service",
    tags=["Note Service"],
    route_class=DishkaRoute,
)


@router.get("/ping")
async def pong(
    request: Request,
    config: FromDishka[Config],
):
    resp = httpx.get(f"{config.service.NOTE_URL}/ping")
    if resp.status_code == status.HTTP_200_OK:
        return resp.json()
    return Response({"detail": "note service not available"})
