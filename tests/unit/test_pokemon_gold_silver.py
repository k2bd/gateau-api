from typing import Optional

import pytest

from gateau_api.game_ram.cartridge_info import ChangeMeaning
from gateau_api.game_ram.pokemon.constants import (
    AERODACTYL_OWNED,
    BELLSPROUT_OWNED,
    BLISSEY_OWNED,
    CELEBI_OWNED,
    CHANSEY_OWNED,
    CHIKORITA_OWNED,
    GOLDEEN_OWNED,
    GRIMER_SEEN,
    JIRACHI_OWNED,
    KABUTO_OWNED,
    KABUTOPS_OWNED,
    LAPRAS_OWNED,
    MEW_OWNED,
    MEWTWO_OWNED,
    ODDISH_OWNED,
    OMANYTE_OWNED,
    OMASTAR_OWNED,
    POLITOED_OWNED,
    RHYHORN_OWNED,
)
from gateau_api.game_ram.pokemon.gold_silver import PokemonGoldSilverInfo


@pytest.mark.parametrize(
    "meaning, expected_address",
    [
        (ODDISH_OWNED, 0xDBEE),
        (BELLSPROUT_OWNED, 0xDBEB),
        (GRIMER_SEEN, 0xDC12),
        (CHIKORITA_OWNED, 0xDBE4),
        (JIRACHI_OWNED, None),
    ],
)
def test_pokemon_gold_silver_byte_for_meaning(meaning: str, expected_address: int):
    assert PokemonGoldSilverInfo.byte_for_meaning(meaning=meaning) == expected_address


@pytest.mark.parametrize(
    "change_address, old_value, new_value, expected_meaning",
    [
        (
            0xDBFD,
            0b11011111,
            0b11111111,
            [ChangeMeaning(meaning=RHYHORN_OWNED, value=True)],
        ),
        (
            0xDBFF,
            0b00000000,
            0b00000100,
            [ChangeMeaning(meaning=LAPRAS_OWNED, value=True)],
        ),
        (  # One pokemon caught, another de-caught
            0xDBED,
            0b11110000,
            0b11010100,
            [
                ChangeMeaning(meaning=GOLDEEN_OWNED, value=False),
                ChangeMeaning(meaning=POLITOED_OWNED, value=True),
            ],
        ),
        (
            0xDBFF,
            None,
            0b11010100,
            [
                ChangeMeaning(meaning=AERODACTYL_OWNED, value=True),
                ChangeMeaning(meaning=KABUTOPS_OWNED, value=True),
                ChangeMeaning(meaning=KABUTO_OWNED, value=False),
                ChangeMeaning(meaning=OMASTAR_OWNED, value=True),
                ChangeMeaning(meaning=OMANYTE_OWNED, value=False),
                ChangeMeaning(meaning=LAPRAS_OWNED, value=True),
                ChangeMeaning(meaning=BLISSEY_OWNED, value=False),
                ChangeMeaning(meaning=CHANSEY_OWNED, value=False),
            ],
        ),
        (  # N.B. last bit has no meaning so only expect 7 values
            0xDC03,
            None,
            0b11010100,
            [
                ChangeMeaning(meaning=CELEBI_OWNED, value=True),
                ChangeMeaning(meaning=MEW_OWNED, value=False),
                ChangeMeaning(meaning=MEWTWO_OWNED, value=False),
            ],
        ),
    ],
)
def test_pokemon_gold_silver_meaning_for_byte_change(
    change_address: int,
    old_value: Optional[int],
    new_value: int,
    expected_meaning: str,
):
    assert (
        PokemonGoldSilverInfo.meaning_for_byte_change(
            address=change_address,
            old_value=old_value,
            new_value=new_value,
        )
        == expected_meaning
    )
