"""Discover and control smart plugs and smart bulbs"""
import asyncio

from .discover import Discover

devices = asyncio.run(Discover.discover())

deviceIPsByName = {}

for ip, alias in devices.items():
    #print(alias.sys_info['alias'])
    deviceAlias = alias.sys_info['alias']
    deviceIPsByName[deviceAlias] = ip

livingRoomLampOneName = 'Living Room Lamp 1'
livingRoomLampTwoName = 'Living Room Lamp 2'
northPorchLightName = 'North Porch Light'
southPorchLightName = 'South Porch Light'

livingRoomLampOneIP = deviceIPsByName[livingRoomLampOneName]
livingRoomLampTwoIP = deviceIPsByName[livingRoomLampTwoName]

livingRoomLampOne = devices[deviceIPsByName[livingRoomLampOneName]]
livingRoomLampTwo = devices[deviceIPsByName[livingRoomLampTwoName]]
northPorchLight = devices[deviceIPsByName[northPorchLightName]]
southPorchLight = devices[deviceIPsByName[southPorchLightName]]


def turn_on_living_room_lights():
    asyncio.run(livingRoomLampOne.turn_on())
    asyncio.run(livingRoomLampTwo.turn_on())

def turn_off_living_room_lights():
    asyncio.run(livingRoomLampOne.turn_off())
    asyncio.run(livingRoomLampTwo.turn_off())

#turn_on_living_room_lights()
#turn_off_living_room_lights()