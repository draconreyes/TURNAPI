from app.core.models import Turn


class TurnQuerysets:

    @staticmethod
    def get_turn_by_date_hour(date: str, hour: str) -> Turn:
        return Turn.objects(date=date, hour=hour).first()

    @staticmethod
    def create_turn(data_turn: dict) -> Turn:
        return Turn(**data_turn).save()

    @staticmethod
    def get_all_turns_by_date(date: str) -> list:
        turns = Turn.objects(date=date)
        json_list = [i.to_json() for i in turns]
        return json_list

    @staticmethod
    def get_turn_by_uuid(uuid: str) -> Turn:
        return Turn.objects(uuid=uuid).first()
