"""Python interface for TP-Link's smart home devices.

All common, shared functionalities are available through `SmartDevice` class::

    x = SmartDevice("192.168.1.1")
    print(x.sys_info)

For device type specific actions `SmartBulb`, `SmartPlug`, or `SmartStrip`
 should be used instead.

Module-specific errors are raised as `SmartDeviceException` and are expected
to be handled by the user of the library.
"""
#from importlib_metadata import version  # type: ignore
from .discover import Discover
from .exceptions import SmartDeviceException
from .protocol import TPLinkSmartHomeProtocol
from .smartbulb import SmartBulb
from .smartdevice import DeviceType, EmeterStatus, SmartDevice
from .smartdimmer import SmartDimmer
from .smartlightstrip import SmartLightStrip
from .smartplug import SmartPlug
from .smartstrip import SmartStrip

#__version__ = version("python-kasa")


__all__ = [
    "Discover",
    "TPLinkSmartHomeProtocol",
    "SmartBulb",
    "DeviceType",
    "EmeterStatus",
    "SmartDevice",
    "SmartDeviceException",
    "SmartPlug",
    "SmartStrip",
    "SmartDimmer",
    "SmartLightStrip",
]
