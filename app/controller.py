from uuid import uuid4

from zmq import device
from app.command import Command
from app.device import Device


class HouseController:
    def __init__(self) -> None:
        self.devices: dict[str, Device] = {}

    def __generate_id(self) -> str:
        return uuid4()

    def register_device(self, device: Device) -> str:
        device_id = self.__generate_id()
        device.connect()
        self.devices[device_id] = device

        return device_id

    def unregister_device(self, device_id: str) -> None:
        self.devices[device_id].disconnect()
        del self.devices[device_id]

    def execute(self, commands: list[Command]) -> None:
        print("----- Starting Execution -----")
        for cmd in commands:
            self.devices[cmd.device_id].send_event(cmd.event, cmd.data)
        print("----- End of Execution -----")
