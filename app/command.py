from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional


class EventType(Enum):
    TURN_ON = auto()
    TURN_OFF = auto()
    PLAY = auto()
    GET_WEATHER = auto()


@dataclass
class Command:
    device_id: str
    event: EventType
    data: str = ""
