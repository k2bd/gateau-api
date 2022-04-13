from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from fastapi_camelcase import CamelModel
from pydantic import Field

from gateau_api.game_ram.carts import Cartridge


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

    #: Player UID
    uid: str

    #: Cartridge the player is using
    cartridge: Cartridge

    #: Player colour for marks
    color: str

    #: Display name of the player
    name: Optional[str]

    #: Photo URL of the player
    photo_url: Optional[str]


def _now_iso():
    return datetime.utcnow().isoformat() + "Z"


class GameEvent(CamelModel):
    """
    An individual game event
    """

    #: Meaning of the event
    meaning: str

    #: Value
    value: Union[str, int, bool]

    #: Player name
    player_id: str

    #: UTC timestamp of the event update, in ISO format
    timestamp: str = Field(default_factory=_now_iso)


class PokemonAvatar(CamelModel):
    """
    A Pokemon avatar someone can use
    """

    #: National dex number
    national_dex: int

    #: If the user can use shiny Pokemon
    allow_shiny: bool

    #: The reason the player can use this avatar
    grant_reason: Optional[str]


class FirebaseUser(CamelModel):
    """
    A user of the Gateau platform
    """

    #: UID
    uid: str

    #: Custom claims
    claims: Optional[Dict[str, Any]]

    #: Display name
    display_name: Optional[str]

    #: Email
    email: Optional[str]

    #: Display photo
    photo_url: Optional[str]

    #: Available bonus avatars
    avatars: List[PokemonAvatar]
