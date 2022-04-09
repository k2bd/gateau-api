from typing import Optional

import pytest
from firebasil.auth.types import SignUpUser
from freezegun import freeze_time

from gateau_api.exceptions import PlayerNotFound
from gateau_api.game_ram.carts import Cartridge
from gateau_api.game_ram.pokemon.constants import (
    CHARMANDER_SEEN,
    CHARMELEON_SEEN,
    GLOOM_OWNED,
    GOLBAT_OWNED,
    JIRACHI_SEEN,
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
from tests.integration.constants import (
    EXAMPLE_USER_DISPLAY_NAME,
    EXAMPLE_USER_PHOTO_URL,
)


@pytest.mark.parametrize("player_name", [EXAMPLE_USER_DISPLAY_NAME, None])
@pytest.mark.parametrize("photo_url", [EXAMPLE_USER_PHOTO_URL, None])
@pytest.mark.asyncio
async def test_set_and_get_player(
    service: GateauFirebaseService,
    example_user: SignUpUser,
    player_name: Optional[str],
    photo_url: Optional[str],
):
    player = Player(
        uid=example_user.local_id,
        cartridge=Cartridge.POKEMON_RED,
        color="#11AA55",
        name=player_name,
        photo_url=photo_url,
    )

    await service.join_game("game123", player)

    assert await service.get_player("game123", example_user.local_id) == player


@pytest.mark.asyncio
async def test_remove_player(
    service: GateauFirebaseService,
    example_user: SignUpUser,
):
    player = Player(
        uid=example_user.local_id, cartridge=Cartridge.POKEMON_RED, color="#11AA55"
    )

    await service.join_game("game123", player)

    await service.remove_player("game123", example_user.local_id)

    with pytest.raises(PlayerNotFound):
        assert await service.get_player("game123", example_user.local_id)


@pytest.mark.asyncio
async def test_add_and_get_subscriptions(
    service: GateauFirebaseService,
    example_user: SignUpUser,
):
    subscriptions = {
        CHARMANDER_SEEN,
        MEWTWO_OWNED,
    }
    await service.add_subscriptions("game123", subscriptions)

    assert await service.get_subscriptions("game123") == subscriptions

    new_subscriptions = {
        KAKUNA_OWNED,
        MEWTWO_OWNED,
        SCYTHER_SEEN,
    }
    await service.add_subscriptions("game123", new_subscriptions)

    assert await service.get_subscriptions("game123") == {
        CHARMANDER_SEEN,
        MEWTWO_OWNED,
        KAKUNA_OWNED,
        SCYTHER_SEEN,
    }


@pytest.mark.asyncio
async def test_add_and_get_events(
    service: GateauFirebaseService,
    example_user: SignUpUser,
):
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
        await service.add_event("game123", event)

    assert await service.get_events("game123") == [event1, event2, event3]


@pytest.mark.asyncio
async def test_get_ram_subscriptions(
    service: GateauFirebaseService,
    example_user: SignUpUser,
):
    subscriptions = {
        CHARMANDER_SEEN,
        CHARMELEON_SEEN,
        MEWTWO_OWNED,
        JIRACHI_SEEN,  # Should be ignored
    }
    await service.add_subscriptions("game123", subscriptions)

    player = Player(
        uid=example_user.local_id,
        cartridge=Cartridge.POKEMON_RED,
        color="#CCBBAA",
    )
    await service.join_game("game123", player)

    ram_subscriptions = await service.get_ram_subscriptions(
        "game123", example_user.local_id
    )

    assert ram_subscriptions == {0xD309, 0xD30A}


@pytest.mark.asyncio
async def test_handle_ram(
    service: GateauFirebaseService,
    example_user: SignUpUser,
):
    player = Player(
        uid=example_user.local_id, cartridge=Cartridge.POKEMON_RED, color="#098765"
    )
    await service.join_game("game123", player)

    change = RamChangeInfo(
        frame=123,
        old_frame=122,
        events=[RamEvent(location=0xD2FC, old=0b00000000, new=0b11111111)],
    )

    frozen_time = "2020-01-02T03:04:05Z"
    with freeze_time(frozen_time):
        await service.handle_ram("game123", example_user.local_id, change_info=change)

    assert await service.get_events("game123") == [
        GameEvent(
            meaning=VENONAT_OWNED,
            value=True,
            player_id=example_user.local_id,
            timestamp=frozen_time,
        ),
        GameEvent(
            meaning=PARASECT_OWNED,
            value=True,
            player_id=example_user.local_id,
            timestamp=frozen_time,
        ),
        GameEvent(
            meaning=PARAS_OWNED,
            value=True,
            player_id=example_user.local_id,
            timestamp=frozen_time,
        ),
        GameEvent(
            meaning=VILEPLUME_OWNED,
            value=True,
            player_id=example_user.local_id,
            timestamp=frozen_time,
        ),
        GameEvent(
            meaning=GLOOM_OWNED,
            value=True,
            player_id=example_user.local_id,
            timestamp=frozen_time,
        ),
        GameEvent(
            meaning=ODDISH_OWNED,
            value=True,
            player_id=example_user.local_id,
            timestamp=frozen_time,
        ),
        GameEvent(
            meaning=GOLBAT_OWNED,
            value=True,
            player_id=example_user.local_id,
            timestamp=frozen_time,
        ),
        GameEvent(
            meaning=ZUBAT_OWNED,
            value=True,
            player_id=example_user.local_id,
            timestamp=frozen_time,
        ),
    ]
