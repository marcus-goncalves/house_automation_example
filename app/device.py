from abc import ABC, abstractmethod
import random
import time

from app.command import EventType


class DeviceContract(ABC):
    def __init__(self, name) -> None:
        self.name: str = name

    @abstractmethod
    def connect(self) -> None:
        ...

    def disconnect(self) -> None:
        ...

    def send_event(self, event: EventType) -> None:
        ...


class LightBulb(DeviceContract):
    """
        Simulates a light bulb device in the house.
    """

    def connect(self) -> None:
        delay = round(random.uniform(0.5, 2.5), 1)

        print(f"Connecting to the {self.name} lightbulb...")
        time.sleep(delay)
        print(f"{self.name} Connected! {delay}s")

    def disconnect(self) -> None:
        delay = round(random.uniform(0.5, 2.5), 1)

        print(f"Disconnecting of the {self.name} lightbulb...")
        time.sleep(delay)
        print(f"{self.name} Disconnected! {delay}s")

    def send_event(self, event: EventType) -> None:
        print(f"{self.name} Received event {event.name}...")
