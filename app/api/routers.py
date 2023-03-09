import json

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import status
from app.api.serializers import (
    TurnCreateSerializer,
    SuccessResponseTurnCreateSerializaer,
    ErrorResponseTurnCreateSerializaer,
    ResponseListTurns
)
from app.api.handlers import TournHandler
from app.core.constants import ERROR_SERVER

router = APIRouter()


@router.get("/", tags=["Root"])
async def root() -> JSONResponse:
    root_content = {
        "title": "TURNS API",
        "author": "DIEGO ALEJANDRO PENA REYES",
        "contact": "draconreyes@gmail.com",
        "version": "v1",
        "docs": "/docs",
        }
    return JSONResponse(content=root_content, status_code=status.HTTP_200_OK)


@router.get("/health", tags=["Health"])
async def health() -> JSONResponse:
    health_content = {
        "status": "ok"
        }
    return JSONResponse(content=health_content, status_code=status.HTTP_200_OK)


@router.post("/turn",
             tags=["Turn"],
             responses={
                    200: {
                         "model": SuccessResponseTurnCreateSerializaer,
                         "description": "Success response"
                         },
                    409: {
                         "model": ErrorResponseTurnCreateSerializaer,
                         "description": "Error response"
                         }
                    }
             )
async def create_turn(turn: TurnCreateSerializer) -> JSONResponse:
    try:
        request = json.loads(turn.json())
        data_response, status_code_response = TournHandler.create_turn(request)
        return JSONResponse(
            content=data_response,
            status_code=status_code_response
            )
    except Exception:
        return JSONResponse(
            {"error": ERROR_SERVER},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@router.get(
            '/turn/{date}',
            tags=["Turn"],
            description="list turns by date",
            responses={
                    200: {
                         "model": ResponseListTurns,
                         "description": "Success response"
                         }
                    }
            )
async def list_turns(date: str) -> JSONResponse:
    try:
        data_response, status_code_response = TournHandler.list_turns(date)
        return JSONResponse(
            content=data_response,
            status_code=status_code_response
            )

    except Exception:
        return JSONResponse(
            {"error": ERROR_SERVER},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@router.get(
            '/turn/uuid/{id}',
            tags=["Turn"],
            description="list turns by date",
            responses={
                    200: {
                         "model": SuccessResponseTurnCreateSerializaer,
                         "description": "Success response"
                         },
                    404: {
                         "model": ErrorResponseTurnCreateSerializaer,
                         "description": "Success response"
                        }
                    }
            )
async def get_turn(uuid: str) -> JSONResponse:
    try:
        data_response, status_code_response = TournHandler.get_turn(uuid)
        return JSONResponse(
            content=data_response,
            status_code=status_code_response
            )

    except Exception:
        return JSONResponse(
            {"error": ERROR_SERVER},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
