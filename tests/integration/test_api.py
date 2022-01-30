from fastapi.testclient import TestClient
from freezegun import freeze_time

from gateau_api.game_ram.carts import Cartridge
from gateau_api.game_ram.pokemon.constants import (
    ARBOK_OWNED,
    CHARMANDER_SEEN,
    CHARMELEON_SEEN,
    DROWZEE_OWNED,
    GOLEM_OWNED,
    HITMONCHAN_OWNED,
    HITMONLEE_OWNED,
    MAGMAR_OWNED,
    MEWTWO_OWNED,
    PARASECT_OWNED,
    PSYDUCK_OWNED,
    SCYTHER_OWNED,
)
from gateau_api.service import GateauFirebaseService
from gateau_api.types import GameEvent, Player, RamChangeInfo, RamEvent


def test_post_player_200(
    api_client: TestClient,
    service: GateauFirebaseService,
):
    response = api_client.post(
        "/game/gameABC/players",
        json={"uid": "playerABC", "name": "Player 1", "cartridge": "Pokemon Red"},
    )
    assert response.status_code == 200

    assert service.get_player("gameABC", "playerABC") == Player(
        uid="playerABC",
        name="Player 1",
        cartridge="Pokemon Red",
    )


def test_post_new_subscriptions_200(
    api_client: TestClient,
    service: GateauFirebaseService,
):
    response = api_client.post(
        "/game/gameABC/subscriptions",
        json={"subscriptions": [SCYTHER_OWNED, MEWTWO_OWNED]},
    )
    assert response.status_code == 200

    assert service.get_subscriptions("gameABC") == {SCYTHER_OWNED, MEWTWO_OWNED}


def test_get_ram_subscriptions_200(
    api_client: TestClient,
    service: GateauFirebaseService,
):
    subscriptions = {
        CHARMANDER_SEEN,
        CHARMELEON_SEEN,
        MEWTWO_OWNED,
    }
    service.add_subscriptions("game123", subscriptions)

    player = Player(
        uid="player123",
        name="John Player",
        cartridge=Cartridge.POKEMON_RED,
    )
    service.set_player("game123", player)

    response = api_client.get(
        "/game/game123/ramSubscriptions",
        headers={"player-id": "player123"},
    )

    assert response.status_code == 200
    assert response.json() == {"ramAddresses": [0xD304, 0xD31B]}


def test_post_ram_change_200(
    api_client: TestClient,
    service: GateauFirebaseService,
):
    player = Player(
        uid="player123",
        name="John Player",
        cartridge=Cartridge.POKEMON_RED,
    )
    service.set_player("game123", player)

    change = RamChangeInfo(
        frame=123,
        old_frame=122,
        events=[RamEvent(location=0xD2FC, old=0b00000000, new=0b11111111)],
    )

    frozen_time = "2020-01-02T03:04:05Z"
    with freeze_time(frozen_time):
        response = api_client.post(
            "/game/game123/ramChange",
            headers={"player-id": "player123"},
            json=change.dict(),
        )

    assert response.status_code == 200

    assert service.get_events("game123") == [
        GameEvent(
            meaning=HITMONLEE_OWNED,
            value=True,
            player_id="player123",
            timestamp=frozen_time,
        ),
        GameEvent(
            meaning=HITMONCHAN_OWNED,
            value=True,
            player_id="player123",
            timestamp=frozen_time,
        ),
        GameEvent(
            meaning=ARBOK_OWNED,
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
            meaning=PSYDUCK_OWNED,
            value=True,
            player_id="player123",
            timestamp=frozen_time,
        ),
        GameEvent(
            meaning=DROWZEE_OWNED,
            value=True,
            player_id="player123",
            timestamp=frozen_time,
        ),
        GameEvent(
            meaning=GOLEM_OWNED,
            value=True,
            player_id="player123",
            timestamp=frozen_time,
        ),
        GameEvent(
            meaning=MAGMAR_OWNED,
            value=True,
            player_id="player123",
            timestamp=frozen_time,
        ),
    ]
