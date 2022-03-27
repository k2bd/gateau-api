from typing import Optional

import pytest

from gateau_api.game_ram.cartridge_info import ChangeMeaning
from gateau_api.game_ram.pokemon.constants import (
    BELLSPROUT_OWNED,
    CHANSEY_OWNED,
    CHIKORITA_OWNED,
    DRAGONAIR_SEEN,
    DRAGONITE_SEEN,
    DRATINI_SEEN,
    GOLDEEN_OWNED,
    GRIMER_SEEN,
    HORSEA_OWNED,
    KANGASKHAN_OWNED,
    LAPRAS_OWNED,
    MEW_SEEN,
    MEWTWO_SEEN,
    MOLTRES_SEEN,
    ODDISH_OWNED,
    OWN_25_32,
    RHYHORN_OWNED,
    SEADRA_OWNED,
    SEAKING_OWNED,
    SEEN_33_40,
    STARYU_OWNED,
    TANGELA_OWNED,
    ZAPDOS_SEEN,
)
from gateau_api.game_ram.pokemon.red_blue import PokemonRedBlueInfo


@pytest.mark.parametrize(
    "meaning, expected_address",
    [
        (OWN_25_32, 0xD2FA),
        (SEEN_33_40, 0xD30E),
        (ODDISH_OWNED, 0xD2FC),
        (BELLSPROUT_OWNED, 0xD2FF),
        (GRIMER_SEEN, 0xD314),
        (CHIKORITA_OWNED, None),
    ],
)
def test_pokemon_red_blue_byte_for_meaning(meaning: str, expected_address: int):
    assert PokemonRedBlueInfo.byte_for_meaning(meaning=meaning) == expected_address


@pytest.mark.parametrize(
    "change_address, old_value, new_value, expected_meaning",
    [
        (
            0xD304,
            0b10111111,
            0b11111111,
            [ChangeMeaning(meaning=RHYHORN_OWNED, value=True)],
        ),
        (
            0xD307,
            0b00000000,
            0b00000100,
            [ChangeMeaning(meaning=LAPRAS_OWNED, value=True)],
        ),
        (  # One pokemon caught, another de-caught
            0xD305,
            0b11110000,
            0b11010100,
            [
                ChangeMeaning(meaning=GOLDEEN_OWNED, value=False),
                ChangeMeaning(meaning=KANGASKHAN_OWNED, value=True),
            ],
        ),
        (
            0xD305,
            None,
            0b11010100,
            [
                ChangeMeaning(meaning=STARYU_OWNED, value=True),
                ChangeMeaning(meaning=SEAKING_OWNED, value=True),
                ChangeMeaning(meaning=GOLDEEN_OWNED, value=False),
                ChangeMeaning(meaning=SEADRA_OWNED, value=True),
                ChangeMeaning(meaning=HORSEA_OWNED, value=False),
                ChangeMeaning(meaning=KANGASKHAN_OWNED, value=True),
                ChangeMeaning(meaning=TANGELA_OWNED, value=False),
                ChangeMeaning(meaning=CHANSEY_OWNED, value=False),
            ],
        ),
        (  # N.B. last bit has no meaning so only expect 7 values
            0xD31C,
            None,
            0b11010100,
            [
                ChangeMeaning(meaning=MEW_SEEN, value=True),
                ChangeMeaning(meaning=MEWTWO_SEEN, value=False),
                ChangeMeaning(meaning=DRAGONITE_SEEN, value=True),
                ChangeMeaning(meaning=DRAGONAIR_SEEN, value=False),
                ChangeMeaning(meaning=DRATINI_SEEN, value=True),
                ChangeMeaning(meaning=MOLTRES_SEEN, value=False),
                ChangeMeaning(meaning=ZAPDOS_SEEN, value=False),
            ],
        ),
    ],
)
def test_pokemon_red_blue_meaning_for_byte_change(
    change_address: int,
    old_value: Optional[int],
    new_value: int,
    expected_meaning: str,
):
    assert (
        PokemonRedBlueInfo.meaning_for_byte_change(
            address=change_address,
            old_value=old_value,
            new_value=new_value,
        )
        == expected_meaning
    )
