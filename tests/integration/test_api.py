from typing import Optional

import pytest
from fastapi.testclient import TestClient
from firebasil.auth.types import SignUpUser
from freezegun import freeze_time

from gateau_api.exceptions import PlayerNotFound
from gateau_api.game_ram.carts import Cartridge
from gateau_api.game_ram.pokemon.constants import (
    ABSOL_OWNED,
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
from gateau_api.types import GameEvent, Player, PokemonAvatar, RamChangeInfo, RamEvent
from tests.integration.constants import (
    EXAMPLE_ADMIN_DISPLAY_NAME,
    EXAMPLE_ADMIN_EMAIL,
    EXAMPLE_ADMIN_PHOTO_URL,
    EXAMPLE_USER_DISPLAY_NAME,
    EXAMPLE_USER_EMAIL,
    EXAMPLE_USER_PHOTO_URL,
)


@pytest.mark.parametrize("player_name", [EXAMPLE_USER_DISPLAY_NAME, None])
@pytest.mark.asyncio
async def test_post_player_200(
    api_client: TestClient,
    service: GateauFirebaseService,
    example_user: SignUpUser,
    player_name: Optional[str],
):
    response = api_client.post(
        "/game/gameABC/players",
        json={
            "uid": example_user.local_id,
            "cartridge": "Pokemon Red",
            "color": "#123456",
            "name": player_name,
        },
        headers={"Authorization": f"Bearer {example_user.id_token}"},
    )
    assert response.status_code == 200, response.content

    assert await service.get_player("gameABC", example_user.local_id) == Player(
        uid=example_user.local_id,
        cartridge="Pokemon Red",
        color="#123456",
        name=player_name,
    )


@pytest.mark.asyncio
async def test_delete_player_200(
    api_client: TestClient,
    service: GateauFirebaseService,
    example_user: SignUpUser,
):
    player = Player(
        uid=example_user.local_id,
        cartridge=Cartridge.POKEMON_RED,
        color="#11AA55",
        name=EXAMPLE_USER_DISPLAY_NAME,
    )

    await service.join_game("game123", player)

    response = api_client.delete(
        "/game/gameABC/players",
        headers={"Authorization": f"Bearer {example_user.id_token}"},
    )
    assert response.status_code == 200, response.content

    with pytest.raises(PlayerNotFound):
        assert await service.get_player("gameABC", example_user.local_id)


@pytest.mark.asyncio
async def test_post_new_subscriptions_200(
    api_client: TestClient,
    service: GateauFirebaseService,
    example_user: SignUpUser,
):
    response = api_client.post(
        "/game/gameABC/subscriptions",
        json={"subscriptions": [SCYTHER_OWNED, MEWTWO_OWNED]},
        headers={"Authorization": f"Bearer {example_user.id_token}"},
    )
    assert response.status_code == 200, response.content

    assert await service.get_subscriptions("gameABC") == {SCYTHER_OWNED, MEWTWO_OWNED}


@pytest.mark.asyncio
async def test_get_ram_subscriptions_200(
    api_client: TestClient,
    service: GateauFirebaseService,
    example_user: SignUpUser,
):
    subscriptions = {
        CHARMANDER_SEEN,
        CHARMELEON_SEEN,
        MEWTWO_OWNED,
        ABSOL_OWNED,  # Should be ignored
    }
    await service.add_subscriptions("game123", subscriptions)

    player = Player(
        uid=example_user.local_id,
        cartridge=Cartridge.POKEMON_RED,
        color="#ABCDEF",
        name=EXAMPLE_USER_DISPLAY_NAME,
    )
    await service.join_game("game123", player)

    response = api_client.get(
        "/game/game123/ramSubscriptions",
        headers={"Authorization": f"Bearer {example_user.id_token}"},
    )

    assert response.status_code == 200, response.content
    assert response.json() == {"ramAddresses": [0xD309, 0xD30A]}


@pytest.mark.asyncio
async def test_post_ram_change_200(
    api_client: TestClient,
    service: GateauFirebaseService,
    example_user: SignUpUser,
):
    player = Player(
        uid=example_user.local_id,
        cartridge=Cartridge.POKEMON_RED,
        color="#123ABC",
        name=EXAMPLE_USER_DISPLAY_NAME,
    )
    await service.join_game("game123", player)

    change = RamChangeInfo(
        frame=123,
        old_frame=122,
        events=[RamEvent(location=0xD2FC, old=0b00000000, new=0b11111111)],
    )

    frozen_time = "2020-01-02T03:04:05Z"
    with freeze_time(frozen_time):
        response = api_client.post(
            "/game/game123/ramChange",
            headers={"Authorization": f"Bearer {example_user.id_token}"},
            json=change.dict(),
        )

    assert response.status_code == 200, response.content

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


@pytest.mark.asyncio
async def test_admin_get_users_401(
    api_client: TestClient,
    example_user: SignUpUser,
):
    """
    User is not admin
    """
    response = api_client.get(
        "/admin/users",
        headers={"Authorization": f"Bearer {example_user.id_token}"},
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "You must be an admin."}


@pytest.mark.asyncio
async def test_admin_get_users_200(
    api_client: TestClient,
    example_user: SignUpUser,
    example_admin: SignUpUser,
):
    """
    Admins can get user info
    """
    response = api_client.get(
        "/admin/users",
        headers={"Authorization": f"Bearer {example_admin.id_token}"},
    )
    assert response.status_code == 200
    expected = [
        {
            "uid": example_user.local_id,
            "displayName": EXAMPLE_USER_DISPLAY_NAME,
            "photoUrl": EXAMPLE_USER_PHOTO_URL,
            "email": EXAMPLE_USER_EMAIL,
            "claims": None,
            "avatars": [],
        },
        {
            "uid": example_admin.local_id,
            "displayName": EXAMPLE_ADMIN_DISPLAY_NAME,
            "photoUrl": EXAMPLE_ADMIN_PHOTO_URL,
            "email": EXAMPLE_ADMIN_EMAIL,
            "claims": {"admin": True},
            "avatars": [],
        },
    ]
    assert sorted(response.json(), key=lambda i: i["uid"]) == sorted(
        expected, key=lambda i: i["uid"]
    )


@pytest.mark.asyncio
async def test_user_get_avatars_200(
    api_client: TestClient,
    example_user: SignUpUser,
    example_admin: SignUpUser,
):
    """
    Users can get the avatars available to them
    """
    avatar1 = PokemonAvatar(
        national_dex=25,
        allow_shiny=True,
        grant_reason="Reason 1",
    )
    avatar2 = PokemonAvatar(
        national_dex=26,
        allow_shiny=False,
        grant_reason=None,
    )
    avatar3 = PokemonAvatar(
        national_dex=27,
        allow_shiny=True,
        grant_reason="Reason 2",
    )
    for avatar in [avatar1, avatar2, avatar3]:
        response = api_client.post(
            "admin/avatar",
            headers={"Authorization": f"Bearer {example_admin.id_token}"},
            params={"userId": example_user.local_id},
            json=avatar.dict(),
        )
        assert response.status_code == 200

    response = api_client.get(
        "/user/avatars",
        headers={"Authorization": f"Bearer {example_user.id_token}"},
    )
    assert response.status_code == 200
    expected = [
        {
            "allowShiny": True,
            "grantReason": "Reason 1",
            "nationalDex": 25,
        },
        {
            "allowShiny": False,
            "grantReason": None,
            "nationalDex": 26,
        },
        {
            "allowShiny": True,
            "grantReason": "Reason 2",
            "nationalDex": 27,
        },
    ]
    assert sorted(response.json(), key=lambda i: i["nationalDex"]) == expected


@pytest.mark.asyncio
async def test_avatars(
    api_client: TestClient,
    example_user: SignUpUser,
    example_admin: SignUpUser,
):
    """
    Admins can grant avatars to users
    """
    avatar1 = PokemonAvatar(
        national_dex=25,
        allow_shiny=True,
        grant_reason="Reason 1",
    )
    avatar2 = PokemonAvatar(
        national_dex=26,
        allow_shiny=False,
        grant_reason=None,
    )
    avatar3 = PokemonAvatar(
        national_dex=27,
        allow_shiny=True,
        grant_reason="Reason 2",
    )
    for avatar in [avatar1, avatar2, avatar3]:
        response = api_client.post(
            "admin/avatar",
            headers={"Authorization": f"Bearer {example_admin.id_token}"},
            params={"userId": example_user.local_id},
            json=avatar.dict(),
        )
        assert response.status_code == 200

    response = api_client.get(
        "/admin/users",
        headers={"Authorization": f"Bearer {example_admin.id_token}"},
    )
    assert response.status_code == 200
    expected = [
        {
            "uid": example_user.local_id,
            "displayName": EXAMPLE_USER_DISPLAY_NAME,
            "photoUrl": EXAMPLE_USER_PHOTO_URL,
            "email": EXAMPLE_USER_EMAIL,
            "claims": None,
            "avatars": [
                {
                    "allowShiny": True,
                    "grantReason": "Reason 1",
                    "nationalDex": 25,
                },
                {
                    "allowShiny": False,
                    "grantReason": None,
                    "nationalDex": 26,
                },
                {
                    "allowShiny": True,
                    "grantReason": "Reason 2",
                    "nationalDex": 27,
                },
            ],
        },
        {
            "uid": example_admin.local_id,
            "displayName": EXAMPLE_ADMIN_DISPLAY_NAME,
            "photoUrl": EXAMPLE_ADMIN_PHOTO_URL,
            "email": EXAMPLE_ADMIN_EMAIL,
            "claims": {"admin": True},
            "avatars": [],
        },
    ]
    assert sorted(response.json(), key=lambda i: i["uid"]) == sorted(
        expected, key=lambda i: i["uid"]
    )

    assert (
        api_client.delete(
            "admin/avatar",
            headers={"Authorization": f"Bearer {example_admin.id_token}"},
            params={"userId": example_user.local_id},
            json=avatar2.dict(),
        ).status_code
        == 200
    )
    assert (
        api_client.delete(
            "admin/avatar",
            headers={"Authorization": f"Bearer {example_admin.id_token}"},
            params={"userId": example_user.local_id},
            json=avatar1.dict(),
        ).status_code
        == 200
    )

    response = api_client.get(
        "/admin/users",
        headers={"Authorization": f"Bearer {example_admin.id_token}"},
    )
    assert response.status_code == 200
    expected = [
        {
            "uid": example_user.local_id,
            "displayName": EXAMPLE_USER_DISPLAY_NAME,
            "photoUrl": EXAMPLE_USER_PHOTO_URL,
            "email": EXAMPLE_USER_EMAIL,
            "claims": None,
            "avatars": [
                {
                    "allowShiny": True,
                    "grantReason": "Reason 2",
                    "nationalDex": 27,
                },
            ],
        },
        {
            "uid": example_admin.local_id,
            "displayName": EXAMPLE_ADMIN_DISPLAY_NAME,
            "photoUrl": EXAMPLE_ADMIN_PHOTO_URL,
            "email": EXAMPLE_ADMIN_EMAIL,
            "claims": {"admin": True},
            "avatars": [],
        },
    ]
