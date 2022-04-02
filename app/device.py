from abc import ABC, abstractmethod
import random
import time
import asyncio

from app.command import EventType
from typing import Optional


class Device(ABC):
    def __init__(self, name) -> None:
        self.name: str = name

    @abstractmethod
    def connect(self) -> None:
        ...

    def disconnect(self) -> None:
        ...

    def send_event(self, event: EventType, data: str = "") -> None:
        ...


class LightBulb(Device):
    """
        Simulates a light bulb device in the house.
    """

    async def connect(self) -> None:
        delay = round(random.uniform(0.5, 2.5), 1)

        print(f"Connecting to the {self.name} lightbulb...")
        await asyncio.sleep(delay)
        print(f"{self.name} Connected! {delay}s")

    async def disconnect(self) -> None:
        delay = round(random.uniform(0.5, 2.5), 1)

        print(f"Disconnecting of the {self.name} lightbulb...")
        await asyncio.sleep(delay)
        print(f"{self.name} Disconnected! {delay}s")

    def send_event(self, event: EventType, data: str = "") -> None:
        print(f"{self.name} Received event {event.name} with data {data}...")


class EchoDot(Device):
    """
        Simulates an EchoDot device in the house.
    """

    async def connect(self) -> None:
        delay = round(random.uniform(0.5, 2.5), 1)

        print(f"Connecting to the {self.name} Echo...")
        await asyncio.sleep(delay)
        print(f"{self.name} Connected! {delay}s")

    async def disconnect(self) -> None:
        delay = round(random.uniform(0.5, 2.5), 1)

        print(f"Disconnecting of the {self.name} Echo...")
        await asyncio.sleep(delay)
        print(f"{self.name} Disconnected! {delay}s")

    def send_event(self, event: EventType, data: str = "") -> None:
        print(f"{self.name} Received event {event.name} with data {data}...")
