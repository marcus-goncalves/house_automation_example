from app.command import Command, EventType
from app.controller import HouseController
from app.device import LightBulb


if __name__ == '__main__':
    home = HouseController()

    dinner = LightBulb("dinner room")
    dinner_id = home.register_device(dinner)
    dinner_loop = [
        Command(dinner_id, EventType.TURN_ON),
        Command(dinner_id, EventType.TURN_OFF)
    ]

    tv = LightBulb("tv room")
    tv_id = home.register_device(tv)
    tv_loop = [
        Command(tv_id, EventType.TURN_ON),
        Command(tv_id, EventType.TURN_OFF)
    ]

    home.execute(dinner_loop)
    home.execute(tv_loop)

    home.unregister_device(dinner_id)
    home.unregister_device(tv_id)
