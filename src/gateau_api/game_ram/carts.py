from enum import Enum
from typing import Type

from gateau_api.game_ram.cartridge_info import CartridgeInfo
from gateau_api.game_ram.pokemon.red_blue import PokemonRedBlueInfo


class Cartridge(str, Enum):
    POKEMON_RED = "Pokemon Red"
    POKEMON_BLUE = "Pokemon Blue"


_CARTS = {
    Cartridge.POKEMON_RED: PokemonRedBlueInfo,
    Cartridge.POKEMON_BLUE: PokemonRedBlueInfo,
}


def cart_info(cart: Cartridge) -> Type[CartridgeInfo]:
    return _CARTS[cart]
