from enum import Enum
from typing import Type

from gateau_api.game_ram.cartridge_info import CartridgeInfo
from gateau_api.game_ram.pokemon.crystal import PokemonCrystalInfo
from gateau_api.game_ram.pokemon.gold_silver import PokemonGoldSilverInfo
from gateau_api.game_ram.pokemon.red_blue import PokemonRedBlueInfo


class Cartridge(str, Enum):
    POKEMON_RED = "Pokemon Red"
    POKEMON_BLUE = "Pokemon Blue"
    POKEMON_GOLD = "Pokemon Gold"
    POKEMON_SILVER = "Pokemon Silver"
    POKEMON_CRYSTAL = "Pokemon Crystal"


_CARTS = {
    Cartridge.POKEMON_RED: PokemonRedBlueInfo,
    Cartridge.POKEMON_BLUE: PokemonRedBlueInfo,
    Cartridge.POKEMON_GOLD: PokemonGoldSilverInfo,
    Cartridge.POKEMON_SILVER: PokemonGoldSilverInfo,
    Cartridge.POKEMON_CRYSTAL: PokemonCrystalInfo,
}


def cart_info(cart: Cartridge) -> Type[CartridgeInfo]:
    return _CARTS[cart]
