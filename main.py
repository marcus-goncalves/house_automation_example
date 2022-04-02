import asyncio
from app.command import Command, EventType
from app.controller import HouseController
from app.device import EchoDot, LightBulb


async def main() -> None:
    home = HouseController()

    dinner = LightBulb("Bulb @ dinner room")
    tv = LightBulb("Bulb @ tv room")
    echodot_kitchen = EchoDot("EchoDot @ Kitchen")

    # Gather groups events that will be started "simultaneous"
    dinner_id, tv_id, echodot_id = await asyncio.gather(
        home.register_device(dinner),
        home.register_device(tv),
        home.register_device(echodot_kitchen),
    )

    dinner_loop = [
        Command(dinner_id, EventType.TURN_ON),
        Command(dinner_id, EventType.TURN_OFF)
    ]

    tv_loop = [
        Command(tv_id, EventType.TURN_ON),
        Command(tv_id, EventType.TURN_OFF)
    ]

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

    await asyncio.gather(
        home.unregister_device(dinner_id),
        home.unregister_device(tv_id),
        home.unregister_device(echodot_id)
    )

if __name__ == '__main__':
    asyncio.run(main())
