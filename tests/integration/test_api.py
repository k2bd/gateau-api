from fastapi.testclient import TestClient
from freezegun import freeze_time

from gateau_api.game_ram.carts import Cartridge
from gateau_api.game_ram.pokemon.constants import (
    CHARMANDER_SEEN,
    CHARMELEON_SEEN,
    GLOOM_OWNED,
    GOLBAT_OWNED,
    MEWTWO_OWNED,
    ODDISH_OWNED,
    PARAS_OWNED,
    PARASECT_OWNED,
    SCYTHER_OWNED,
    VENONAT_OWNED,
    VILEPLUME_OWNED,
    ZUBAT_OWNED,
)
from gateau_api.service import GateauFirebaseService
from gateau_api.types import GameEvent, Player, RamChangeInfo, RamEvent
from tests.integration.constants import EXAMPLE_ID_TOKEN, EXAMPLE_USER_ID


def test_post_player_200(
    api_client: TestClient,
    service: GateauFirebaseService,
):
    response = api_client.post(
        "/game/gameABC/players",
        json={"uid": EXAMPLE_USER_ID, "cartridge": "Pokemon Red"},
        headers={"Authorization": f"Bearer {EXAMPLE_ID_TOKEN}"},
    )
    assert response.status_code == 200, response.content

    assert service.get_player("gameABC", EXAMPLE_USER_ID) == Player(
        uid=EXAMPLE_USER_ID,
        cartridge="Pokemon Red",
    )


def test_post_new_subscriptions_200(
    api_client: TestClient,
    service: GateauFirebaseService,
):
    response = api_client.post(
        "/game/gameABC/subscriptions",
        json={"subscriptions": [SCYTHER_OWNED, MEWTWO_OWNED]},
        headers={"Authorization": f"Bearer {EXAMPLE_ID_TOKEN}"},
    )
    assert response.status_code == 200, response.content

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
        uid=EXAMPLE_USER_ID,
        cartridge=Cartridge.POKEMON_RED,
    )
    service.set_player("game123", player)

    response = api_client.get(
        "/game/game123/ramSubscriptions",
        headers={"Authorization": f"Bearer {EXAMPLE_ID_TOKEN}"},
    )

    assert response.status_code == 200, response.content
    assert response.json() == {"ramAddresses": [0xD309, 0xD30A]}


def test_post_ram_change_200(
    api_client: TestClient,
    service: GateauFirebaseService,
):
    player = Player(
        uid=EXAMPLE_USER_ID,
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
            headers={"Authorization": f"Bearer {EXAMPLE_ID_TOKEN}"},
            json=change.dict(),
        )

    assert response.status_code == 200, response.content

    assert service.get_events("game123") == [
        GameEvent(
            meaning=VENONAT_OWNED,
            value=True,
            player_id=EXAMPLE_USER_ID,
            timestamp=frozen_time,
        ),
        GameEvent(
            meaning=PARASECT_OWNED,
            value=True,
            player_id=EXAMPLE_USER_ID,
            timestamp=frozen_time,
        ),
        GameEvent(
            meaning=PARAS_OWNED,
            value=True,
            player_id=EXAMPLE_USER_ID,
            timestamp=frozen_time,
        ),
        GameEvent(
            meaning=VILEPLUME_OWNED,
            value=True,
            player_id=EXAMPLE_USER_ID,
            timestamp=frozen_time,
        ),
        GameEvent(
            meaning=GLOOM_OWNED,
            value=True,
            player_id=EXAMPLE_USER_ID,
            timestamp=frozen_time,
        ),
        GameEvent(
            meaning=ODDISH_OWNED,
            value=True,
            player_id=EXAMPLE_USER_ID,
            timestamp=frozen_time,
        ),
        GameEvent(
            meaning=GOLBAT_OWNED,
            value=True,
            player_id=EXAMPLE_USER_ID,
            timestamp=frozen_time,
        ),
        GameEvent(
            meaning=ZUBAT_OWNED,
            value=True,
            player_id=EXAMPLE_USER_ID,
            timestamp=frozen_time,
        ),
    ]
