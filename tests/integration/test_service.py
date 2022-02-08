import pytest
from freezegun import freeze_time

from gateau_api.exceptions import PlayerNotFound
from gateau_api.game_ram.carts import Cartridge
from gateau_api.game_ram.pokemon.constants import (
    CHARMANDER_SEEN,
    CHARMELEON_SEEN,
    GLOOM_OWNED,
    GOLBAT_OWNED,
    KAKUNA_OWNED,
    MEWTWO_OWNED,
    ODDISH_OWNED,
    PARAS_OWNED,
    PARASECT_OWNED,
    SCYTHER_SEEN,
    VENONAT_OWNED,
    VILEPLUME_OWNED,
    ZUBAT_OWNED,
)
from gateau_api.service import GateauFirebaseService
from gateau_api.types import GameEvent, Player, RamChangeInfo, RamEvent


def test_set_and_get_player(service: GateauFirebaseService):
    player = Player(uid="player123", cartridge=Cartridge.POKEMON_RED, color="#11AA55")

    service.set_player("game123", player)

    assert service.get_player("game123", "player123") == player


def test_remove_player(service: GateauFirebaseService):
    player = Player(uid="player123", cartridge=Cartridge.POKEMON_RED, color="#11AA55")

    service.set_player("game123", player)

    service.remove_player("game123", "player123")

    with pytest.raises(PlayerNotFound):
        assert service.get_player("game123", "player123")


def test_add_and_get_subscriptions(service: GateauFirebaseService):
    subscriptions = {
        CHARMANDER_SEEN,
        MEWTWO_OWNED,
    }
    service.add_subscriptions("game123", subscriptions)

    assert service.get_subscriptions("game123") == subscriptions

    new_subscriptions = {
        KAKUNA_OWNED,
        MEWTWO_OWNED,
        SCYTHER_SEEN,
    }
    service.add_subscriptions("game123", new_subscriptions)

    assert service.get_subscriptions("game123") == {
        CHARMANDER_SEEN,
        MEWTWO_OWNED,
        KAKUNA_OWNED,
        SCYTHER_SEEN,
    }


def test_add_and_get_events(service: GateauFirebaseService):
    event3 = GameEvent(
        meaning=KAKUNA_OWNED,
        value=True,
        player_id="Jim",
        timestamp="2021-11-03T10:10:10Z",
    )
    event1 = GameEvent(
        meaning=KAKUNA_OWNED,
        value=True,
        player_id="Jones",
        timestamp="2021-11-01T10:10:10Z",
    )
    event2 = GameEvent(
        meaning=SCYTHER_SEEN,
        value=False,
        player_id="Jack",
        timestamp="2021-11-02T10:10:10Z",
    )

    for event in [event3, event1, event2]:
        service.add_event("game123", event)

    assert service.get_events("game123") == [event1, event2, event3]


def test_get_ram_subscriptions(service: GateauFirebaseService):
    subscriptions = {
        CHARMANDER_SEEN,
        CHARMELEON_SEEN,
        MEWTWO_OWNED,
    }
    service.add_subscriptions("game123", subscriptions)

    player = Player(
        uid="player123",
        cartridge=Cartridge.POKEMON_RED,
        color="#CCBBAA",
    )
    service.set_player("game123", player)

    ram_subscriptions = service.get_ram_subscriptions("game123", "player123")

    assert ram_subscriptions == {0xD309, 0xD30A}


def test_handle_ram(service: GateauFirebaseService):
    player = Player(uid="player123", cartridge=Cartridge.POKEMON_RED, color="#098765")
    service.set_player("game123", player)

    change = RamChangeInfo(
        frame=123,
        old_frame=122,
        events=[RamEvent(location=0xD2FC, old=0b00000000, new=0b11111111)],
    )

    frozen_time = "2020-01-02T03:04:05Z"
    with freeze_time(frozen_time):
        service.handle_ram("game123", "player123", change_info=change)

    assert service.get_events("game123") == [
        GameEvent(
            meaning=VENONAT_OWNED,
            value=True,
            player_id="player123",
            timestamp=frozen_time,
        ),
        GameEvent(
            meaning=PARASECT_OWNED,
            value=True,
            player_id="player123",
            timestamp=frozen_time,
        ),
        GameEvent(
            meaning=PARAS_OWNED,
            value=True,
            player_id="player123",
            timestamp=frozen_time,
        ),
        GameEvent(
            meaning=VILEPLUME_OWNED,
            value=True,
            player_id="player123",
            timestamp=frozen_time,
        ),
        GameEvent(
            meaning=GLOOM_OWNED,
            value=True,
            player_id="player123",
            timestamp=frozen_time,
        ),
        GameEvent(
            meaning=ODDISH_OWNED,
            value=True,
            player_id="player123",
            timestamp=frozen_time,
        ),
        GameEvent(
            meaning=GOLBAT_OWNED,
            value=True,
            player_id="player123",
            timestamp=frozen_time,
        ),
        GameEvent(
            meaning=ZUBAT_OWNED,
            value=True,
            player_id="player123",
            timestamp=frozen_time,
        ),
    ]
