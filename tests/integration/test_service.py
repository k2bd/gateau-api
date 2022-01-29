from gateau_api.game_ram.carts import Cartridge
from gateau_api.game_ram.pokemon.constants import (
    CHARMANDER_SEEN,
    KAKUNA_OWNED,
    MEWTWO_OWNED,
    SCYTHER_SEEN,
)
from gateau_api.service import GateauFirebaseService
from gateau_api.types import GameEvent, Player


def test_set_and_get_player(service: GateauFirebaseService):
    player = Player(
        uid="player123",
        name="John Player",
        cartridge=Cartridge.POKEMON_RED,
    )

    service.set_player("game123", player)

    assert service.get_player("game123", "player123") == player


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
        player_name="Jim",
        timestamp="2021-11-03T10:10:10Z",
    )
    event1 = GameEvent(
        meaning=KAKUNA_OWNED,
        value=True,
        player_name="Jones",
        timestamp="2021-11-01T10:10:10Z",
    )
    event2 = GameEvent(
        meaning=SCYTHER_SEEN,
        value=False,
        player_name="Jack",
        timestamp="2021-11-02T10:10:10Z",
    )

    for event in [event3, event1, event2]:
        service.add_event("game123", event)

    assert service.get_events("game123") == [event1, event2, event3]
