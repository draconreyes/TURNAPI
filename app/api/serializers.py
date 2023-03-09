from typing import List
from datetime import date as datetime_date

from pydantic import (
    BaseModel,
    Field,
    validator
    )
from app.core.constants import TurnInterval


class TurnCreateSerializer(BaseModel):
    name: str = Field(..., example="Armando Puertas")
    document: str = Field(..., example="1234567890")
    date: datetime_date = Field(..., example=datetime_date.today())
    hour: TurnInterval = Field(..., example=TurnInterval.EIGHT_AM.value)

    @validator('date')
    def validate_date(cls, v):
        if v < datetime_date.today():
            raise ValueError(
                "The date must be equal or greater than the actual date"
                )
        return v


class SuccessResponseTurnCreateSerializaer(TurnCreateSerializer):
    uuid: str = Field(..., example="UIDASDAS6D5566")


class ErrorResponseTurnCreateSerializaer(BaseModel):
    error: str = Field(..., example="Error response")


class ResponseListTurns(BaseModel):
    data: List[SuccessResponseTurnCreateSerializaer]
