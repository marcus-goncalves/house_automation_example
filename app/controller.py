from uuid import uuid4

from zmq import device
from app.command import Command
from app.device import Device


class HouseController:
    def __init__(self) -> None:
        self.devices: dict[str, Device] = {}

    def __generate_id(self) -> str:
        return uuid4()

    async def register_device(self, device: Device) -> str:
        await device.connect()
        device_id = self.__generate_id()
        self.devices[device_id] = device

        return device_id

    async def unregister_device(self, device_id: str) -> None:
        await self.devices[device_id].disconnect()
        del self.devices[device_id]

    def execute(self, commands: list[Command]) -> None:
        print("----- Starting Execution -----")
        for cmd in commands:
            self.devices[cmd.device_id].send_event(cmd.event, cmd.data)
        print("----- End of Execution -----")
