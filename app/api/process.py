from typing import Union

from fastapi import status
from app.core.querysets import TurnQuerysets
from app.core.constants import (
    ERROR_TURN_IS_BUSY,
    ERROR_TURN_NOT_FOUND
)


class TurnProcess:

    @staticmethod
    def create_turn(request: dict) -> Union[dict, int]:
        is_busy_turn = TurnQuerysets.get_turn_by_date_hour(
                request.get("date"), request.get("hour")
            )
        if is_busy_turn:
            return {"error": ERROR_TURN_IS_BUSY}, status.HTTP_409_CONFLICT
        turn = TurnQuerysets.create_turn(request)
        return turn.to_json(), status.HTTP_200_OK

    @staticmethod
    def get_list_turns_of_day(query_date: str) -> Union[dict, int]:
        json_list = TurnQuerysets.get_all_turns_by_date(query_date)
        return {"data": json_list}, status.HTTP_200_OK

    @staticmethod
    def get_turn_by_uuid(uuid: str) -> Union[dict, int]:
        turn = TurnQuerysets.get_turn_by_uuid(uuid)
        if not turn:
            return {"error": ERROR_TURN_NOT_FOUND}, status.HTTP_404_NOT_FOUND
        return turn.to_json(), status.HTTP_200_OK
