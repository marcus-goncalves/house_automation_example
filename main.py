from app.command import Command, EventType
from app.controller import HouseController
from app.device import Alexa, LightBulb


if __name__ == '__main__':
    home = HouseController()

    dinner = LightBulb("Bulb @ dinner room")
    dinner_id = home.register_device(dinner)
    dinner_loop = [
        Command(dinner_id, EventType.TURN_ON),
        Command(dinner_id, EventType.TURN_OFF)
    ]

    tv = LightBulb("Bulb @ tv room")
    tv_id = home.register_device(tv)
    tv_loop = [
        Command(tv_id, EventType.TURN_ON),
        Command(tv_id, EventType.TURN_OFF)
    ]

    echodot_kitchen = EchoDot("EchoDot @ Kitchen")
    echodot_id = home.register_device(echodot_kitchen)
    echodot_loop = [
        Command(echodot_id, EventType.TURN_ON),
        Command(echodot_id, EventType.PLAY, "Iron Maiden - Aces High"),
        Command(echodot_id, EventType.GET_WEATHER,
                "Belo Horizonte/MG"),
        Command(echodot_id, EventType.TURN_OFF),
    ]

    home.execute(dinner_loop)
    home.execute(tv_loop)
    home.execute(echodot_loop)

    home.unregister_device(dinner_id)
    home.unregister_device(tv_id)
    home.unregister_device(echodot_id)
