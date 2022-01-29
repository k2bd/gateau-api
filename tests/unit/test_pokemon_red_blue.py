import pytest
from gateau_api.game_ram.cartridge_info import ChangeMeaning

from gateau_api.game_ram.pokemon.constants import (
    BELLSPROUT_OWNED,
    ELECTRODE_OWNED,
    GOLDUCK_OWNED,
    GRIMER_SEEN,
    ODDISH_OWNED,
    OWN_25_32,
    PERSIAN_OWNED,
    RATICATE_OWNED,
    SEEN_33_40,
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
            [ChangeMeaning(meaning=GOLDUCK_OWNED, positive=True)],
        ),
        (
            0xD307,
            0b00000000,
            0b00000100,
            [ChangeMeaning(meaning=RATICATE_OWNED, positive=True)],
        ),
        (  # One pokemon caught, another uncaught
            0xD305,
            0b11110000,
            0b11010100,
            [
                ChangeMeaning(meaning=ELECTRODE_OWNED, positive=False),
                ChangeMeaning(meaning=PERSIAN_OWNED, positive=True),
            ],
        ),
    ],
)
def test_pokemon_red_blue_meaning_for_byte_change(
    change_address: int,
    old_value: int,
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
