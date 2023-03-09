from enum import Enum


class TurnInterval(str, Enum):
    EIGHT_AM = '08:00'
    EIGHT_THIRTY_AM = '08:30'
    NINE_AM = '09:00'
    NINE_THIRTY_AM = '09:30'
    TEN_AM = '10:00'
    TEN_THIRTY_AM = '10:30'
    ELEVEN_AM = '11:00'
    ELEVEN_THIRTY_AM = '11:30'
    TWELVE_PM = '12:00'
    TWELVE_THIRTY_PM = '12:30'
    ONE_PM = '13:00'
    ONE_THIRTY_PM = '13:30'
    TWO_PM = '14:00'
    TWO_THIRTY_PM = '14:30'
    THREE_PM = '15:00'
    THREE_THIRTY_PM = '15:30'
    FOUR_PM = '16:00'
    FOUR_THIRTY_PM = '16:30'
    FIVE_PM = '17:00'
# Errors


ERROR_TURN_IS_BUSY = "The turn is busy"
ERROR_SERVER = "Error in the server"
ERROR_TURN_NOT_FOUND = "Turn not found"
