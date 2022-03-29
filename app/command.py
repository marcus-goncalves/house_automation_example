from dataclasses import dataclass
from enum import Enum, auto


class EventType(Enum):
    TURN_ON = auto()
    TURN_OFF = auto()


@dataclass
class Command:
    device_id: str
    event: EventType
