from app.api.process import TurnProcess
from typing import Union


class TournHandler:

    @staticmethod
    def create_turn(request: dict) -> Union[dict, int]:
        return TurnProcess.create_turn(request)

    @staticmethod
    def list_turns(date: str) -> Union[dict, int]:
        return TurnProcess.get_list_turns_of_day(date)

    @staticmethod
    def get_turn(uuid: str) -> Union[dict, int]:
        return TurnProcess.get_turn_by_uuid(uuid)
