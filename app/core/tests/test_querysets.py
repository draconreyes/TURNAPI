import unittest
import mongomock
from mongoengine import connect, disconnect
from app.core.querysets import TurnQuerysets
from app.core.models import Turn



class TestCreateTurn(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connect('mongoenginetest', host='mongodb://localhost', mongo_client_class=mongomock.MongoClient)

    @classmethod
    def tearDownClass(cls):
       disconnect()

    def test_success(self):
        data_turn = {
            "name": "Diego",
            "document": "12456611",
            "date": "2023-03-08",
            "hour": "08:00"
        }
        expected_response = "12456611"

        TurnQuerysets.create_turn(data_turn)
        net_turn = Turn.objects(document=data_turn.get('document')).first()

        assert net_turn.document == expected_response


class TestGetTurnByDateHour(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connect('mongoenginetest', host='mongodb://localhost', mongo_client_class=mongomock.MongoClient)
        data_turn = {
            "name": "Diego",
            "document": "12456611",
            "date": "2023-03-08",
            "hour": "08:00"
        }
        TurnQuerysets.create_turn(data_turn)

    @classmethod
    def tearDownClass(cls):
       disconnect()

    def test_success(self):
        date = "2023-03-08"
        hour = "08:00"
        
        turn = TurnQuerysets.get_turn_by_date_hour(date=date, hour=hour)

        assert turn

    def test_not_found(self):
        date = "2023-03-08"
        hour = "09:00"
        
        turn = TurnQuerysets.get_turn_by_date_hour(date=date, hour=hour)

        assert not turn


class TestGetAllTurnsByDate(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connect('mongoenginetest', host='mongodb://localhost', mongo_client_class=mongomock.MongoClient)
        data_turn_1 = {
            "name": "Diego",
            "document": "12456611",
            "date": "2023-03-08",
            "hour": "08:00"
        }
        data_turn_2 = {
            "name": "Armando",
            "document": "457888",
            "date": "2023-03-08",
            "hour": "09:00"
        }
        TurnQuerysets.create_turn(data_turn_1)
        TurnQuerysets.create_turn(data_turn_2)

    @classmethod
    def tearDownClass(cls):
       disconnect()

    def test_success(self):
        date = "2023-03-08"
        expected_response_1 = "12456611"
        expected_response_2 = "457888"
        
        turns = TurnQuerysets.get_all_turns_by_date(date=date)

        assert expected_response_1 == turns[0].get("document")
        assert expected_response_2 == turns[1].get("document")

    def test_empty_list(self):
        date = "2023-03-09"

        turns = TurnQuerysets.get_all_turns_by_date(date=date)

        assert not turns


class TestGetTurnByUUID(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connect('mongoenginetest', host='mongodb://localhost', mongo_client_class=mongomock.MongoClient)
        data_turn = {
            "name": "Diego",
            "document": "12456611",
            "date": "2023-03-08",
            "hour": "08:00"
        }
        turn = TurnQuerysets.create_turn(data_turn)

    @classmethod
    def tearDownClass(cls):
       disconnect()

    def test_success(self):
        name = "Diego"
        date = "2023-03-08"
        hour = "08:00"

        turn = TurnQuerysets.get_turn_by_date_hour(date=date, hour=hour)
        turn = TurnQuerysets.get_turn_by_uuid(uuid=turn.uuid)

        assert turn.name == name

    def test_not_found(self):
        uuid = "000000000000001"

        turn = TurnQuerysets.get_turn_by_uuid(uuid=uuid)

        assert not turn
