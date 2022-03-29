from abc import ABC, abstractmethod
import random
import time

from app.command import EventType


class DeviceContract(ABC):
    @abstractmethod
    def connect(self) -> None:
        ...

    def disconnect(self) -> None:
        ...

    def send_command(self, event: EventType) -> None:
        ...


class LightBulb(DeviceContract):
    """
        Simulates a light bulb device in the house.
    """

    def connect(self) -> None:
        delay = round(random.uniform(0.5, 2.5), 1)

        print("Connecting to the lightbulb...")
        time.sleep(delay)
        print(f"Connected to the light bulb! {delay}s")

    def disconnect(self) -> None:
        delay = round(random.uniform(0.5, 2.5), 1)

        print("Disconnecting to the lightbulb...")
        time.sleep(delay)
        print(f"Disconnected to the light bulb! {delay}s")

    def send_command(self, event: EventType) -> None:
        print(f"Received cmd {event}...")
