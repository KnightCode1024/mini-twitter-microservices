from fastapi import APIRouter, Request, Response, HTTPException, status
from dishka.integrations.fastapi import FromDishka, DishkaRoute

from services import MessageService
from schemas.message import MessageCreate, MessageUpdate, MessageResponse


router = APIRouter(
    prefix="/messages",
    tags=["Messages"],
    route_class=DishkaRoute,
)


@router.post("/", response_model=MessageResponse)
async def create_msg(
    response: Response,
    request: Request,
    msg_data: MessageCreate,
    service: FromDishka[MessageService],
):
    try:
        return await service.create_msg(msg_data)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{e}",
        )


@router.get("/{msg_id}", response_model=MessageResponse)
async def get_msg(
    response: Response,
    request: Request,
    msg_id: int,
    service: FromDishka[MessageService],
):
    try:
        return await service.get_msg(msg_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{e}",
        )


@router.get("/", response_model=list[MessageResponse])
async def get_all_msg(
    response: Response,
    request: Request,
    service: FromDishka[MessageService],
):
    try:
        return await service.get_all_msgs()
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{e}",
        )


@router.patch("/{msg_id}", response_model=MessageResponse)
async def update_msg(
    response: Response,
    request: Request,
    msg_id: int,
    msg_data: MessageUpdate,
    service: FromDishka[MessageService],
):
    try:
        return await service.update_msg(msg_id, msg_data)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{e}",
        )


@router.delete("/{msg_id}")
async def delete_msg(
    response: Response,
    request: Request,
    msg_id: int,
    service: FromDishka[MessageService],
):
    try:
        return await service.delete_msg(msg_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{e}",
        )
