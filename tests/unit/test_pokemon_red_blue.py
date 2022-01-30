from typing import Optional

import pytest

from gateau_api.game_ram.cartridge_info import ChangeMeaning
from gateau_api.game_ram.pokemon.constants import (
    BELLSPROUT_OWNED,
    BELLSPROUT_SEEN,
    CHARIZARD_SEEN,
    CLEFABLE_OWNED,
    CLOYSTER_OWNED,
    ELECTRODE_OWNED,
    GLOOM_SEEN,
    GOLDUCK_OWNED,
    GRIMER_SEEN,
    HAUNTER_OWNED,
    KINGLER_OWNED,
    MAROWAK_OWNED,
    ODDISH_OWNED,
    ODDISH_SEEN,
    OWN_25_32,
    PERSIAN_OWNED,
    RATICATE_OWNED,
    SEEN_33_40,
    VICTREEBEL_SEEN,
    VILEPLUME_SEEN,
    WEEPINBELL_SEEN,
    WEEZING_OWNED,
)
from gateau_api.game_ram.pokemon.red_blue import PokemonRedBlueInfo


@pytest.mark.parametrize(
    "meaning, expected_address",
    [
        (OWN_25_32, 0xD2FA),
        (SEEN_33_40, 0xD30E),
        (ODDISH_OWNED, 0xD309),
        (BELLSPROUT_OWNED, 0xD309),
        (GRIMER_SEEN, 0xD30B),
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
            [ChangeMeaning(meaning=GOLDUCK_OWNED, value=True)],
        ),
        (
            0xD307,
            0b00000000,
            0b00000100,
            [ChangeMeaning(meaning=RATICATE_OWNED, value=True)],
        ),
        (  # One pokemon caught, another de-caught
            0xD305,
            0b11110000,
            0b11010100,
            [
                ChangeMeaning(meaning=ELECTRODE_OWNED, value=False),
                ChangeMeaning(meaning=PERSIAN_OWNED, value=True),
            ],
        ),
        (
            0xD305,
            None,
            0b11010100,
            [
                ChangeMeaning(meaning=KINGLER_OWNED, value=True),
                ChangeMeaning(meaning=CLOYSTER_OWNED, value=True),
                ChangeMeaning(meaning=ELECTRODE_OWNED, value=False),
                ChangeMeaning(meaning=CLEFABLE_OWNED, value=True),
                ChangeMeaning(meaning=WEEZING_OWNED, value=False),
                ChangeMeaning(meaning=PERSIAN_OWNED, value=True),
                ChangeMeaning(meaning=MAROWAK_OWNED, value=False),
                ChangeMeaning(meaning=HAUNTER_OWNED, value=False),
            ],
        ),
        (  # N.B. last bit has no meaning so only expect 7 values
            0xD31C,
            None,
            0b11010100,
            [
                ChangeMeaning(meaning=CHARIZARD_SEEN, value=True),
                ChangeMeaning(meaning=ODDISH_SEEN, value=True),
                ChangeMeaning(meaning=GLOOM_SEEN, value=False),
                ChangeMeaning(meaning=VILEPLUME_SEEN, value=True),
                ChangeMeaning(meaning=BELLSPROUT_SEEN, value=False),
                ChangeMeaning(meaning=WEEPINBELL_SEEN, value=True),
                ChangeMeaning(meaning=VICTREEBEL_SEEN, value=False),
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
