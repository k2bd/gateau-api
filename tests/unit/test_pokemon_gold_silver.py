from typing import Optional

import pytest

from gateau_api.game_ram.cartridge_info import ChangeMeaning
from gateau_api.game_ram.pokemon.constants import (
    BELLSPROUT_OWNED,
    CELEBI_OWNED,
    CHIKORITA_OWNED,
    CORSOLA_OWNED,
    DUNSPARCE_OWNED,
    GRAVELER_OWNED,
    GRIMER_SEEN,
    HO_OH_OWNED,
    JIRACHI_OWNED,
    LUGIA_OWNED,
    MAGCARGO_OWNED,
    OCTILLERY_OWNED,
    ODDISH_OWNED,
    PILOSWINE_OWNED,
    RAPIDASH_OWNED,
    REMORAID_OWNED,
    SLUGMA_OWNED,
    SWINUB_OWNED,
    URSARING_OWNED,
)
from gateau_api.game_ram.pokemon.gold_silver import PokemonGoldSilverInfo


@pytest.mark.parametrize(
    "meaning, expected_address",
    [
        (ODDISH_OWNED, 0xDBE9),
        (BELLSPROUT_OWNED, 0xDBEC),
        (GRIMER_SEEN, 0xDC0E),
        (CHIKORITA_OWNED, 0xDBF6),
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
            [ChangeMeaning(meaning=DUNSPARCE_OWNED, value=True)],
        ),
        (
            0xDBFF,
            0b00000000,
            0b00000100,
            [ChangeMeaning(meaning=MAGCARGO_OWNED, value=True)],
        ),
        (  # One pokemon caught, another de-caught
            0xDBED,
            0b11110000,
            0b11010100,
            [
                ChangeMeaning(meaning=RAPIDASH_OWNED, value=False),
                ChangeMeaning(meaning=GRAVELER_OWNED, value=True),
            ],
        ),
        (
            0xDBFF,
            None,
            0b11010100,
            [
                ChangeMeaning(meaning=OCTILLERY_OWNED, value=True),
                ChangeMeaning(meaning=REMORAID_OWNED, value=True),
                ChangeMeaning(meaning=CORSOLA_OWNED, value=False),
                ChangeMeaning(meaning=PILOSWINE_OWNED, value=True),
                ChangeMeaning(meaning=SWINUB_OWNED, value=False),
                ChangeMeaning(meaning=MAGCARGO_OWNED, value=True),
                ChangeMeaning(meaning=SLUGMA_OWNED, value=False),
                ChangeMeaning(meaning=URSARING_OWNED, value=False),
            ],
        ),
        (  # N.B. last bit has no meaning so only expect 7 values
            0xDC03,
            None,
            0b11010100,
            [
                ChangeMeaning(meaning=CELEBI_OWNED, value=True),
                ChangeMeaning(meaning=HO_OH_OWNED, value=False),
                ChangeMeaning(meaning=LUGIA_OWNED, value=False),
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
