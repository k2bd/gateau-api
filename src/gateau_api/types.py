from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Optional

from fastapi_camelcase import CamelModel

from gateau_api.game_ram.carts import Cartridge, cart_info


class Subscription(CamelModel):
    """
    A location in memory to subscribe to
    """

    #: RAM addresses to subscribe to changes on
    ram_addresses: List[int]


class GameRoom(CamelModel):
    """
    A Gateau game
    """

    supported_cartridges: List[Cartridge]


class RamEvent(CamelModel):
    """
    A change in a subscribed RAM location
    """

    #: Location in memory
    location: int

    #: Old value, or None if this is the first frame
    old: Optional[int]

    #: New value
    new: int


class RamChangeInfo(CamelModel):
    #: New frame value
    frame: int

    #: Old frame value, if any
    old_frame: Optional[int]

    #: Change events
    events: List[RamEvent]


class Player(CamelModel):
    """
    A player in a Gateau lobby
    """

    #: Player name
    name: str

    #: Cartridge the player is using
    cartridge: Cartridge


class Trackable(CamelModel):
    """
    An individual trackable goal
    """

    #: Kind of goal
    kind: str

    #: Players that have claimed this goal
    claimed_by: List[str]


class Goal(CamelModel):
    """ """
