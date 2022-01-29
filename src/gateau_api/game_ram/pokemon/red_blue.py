from typing import List, Optional, Tuple

from bidict import bidict

from gateau_api.game_ram.cartridge_info import CartridgeInfo, ChangeMeaning

from .constants import *

#: Internal ID to Pokemon (reversible)
ID_TO_POKEMON = bidict(
    {
        0x1: RHYDON,
        0x2: KANGASKHAN,
        0x3: NIDORAN_M,
        0x4: CLEFAIRY,
        0x5: SPEAROW,
        0x6: VOLTORB,
        0x7: NIDOKING,
        0x8: SLOWBRO,
        0x9: IVYSAUR,
        0x0A: EXEGGUTOR,
        0x0B: LICKITUNG,
        0x0C: EXEGGCUTE,
        0x0D: GRIMER,
        0x0E: GENGAR,
        0x0F: NIDORAN_F,
        0x10: NIDOQUEEN,
        0x11: CUBONE,
        0x12: RHYHORN,
        0x13: LAPRAS,
        0x14: ARCANINE,
        0x15: MEW,
        0x16: GYARADOS,
        0x17: SHELLDER,
        0x18: TENTACOOL,
        0x19: GASTLY,
        0x1A: SCYTHER,
        0x1B: STARYU,
        0x1C: BLASTOISE,
        0x1D: PINSIR,
        0x1E: TANGELA,
        0x21: GROWLITHE,
        0x22: ONIX,
        0x23: FEAROW,
        0x24: PIDGEY,
        0x25: SLOWPOKE,
        0x26: KADABRA,
        0x27: GRAVELER,
        0x28: CHANSEY,
        0x29: MACHOKE,
        0x2A: MRMIME,
        0x2B: HITMONLEE,
        0x2C: HITMONCHAN,
        0x2D: ARBOK,
        0x2E: PARASECT,
        0x2F: PSYDUCK,
        0x30: DROWZEE,
        0x31: GOLEM,
        0x33: MAGMAR,
        0x35: ELECTABUZZ,
        0x36: MAGNETON,
        0x37: KOFFING,
        0x39: MANKEY,
        0x3A: SEEL,
        0x3B: DIGLETT,
        0x3C: TAUROS,
        0x40: FARFETCHD,
        0x41: VENONAT,
        0x42: DRAGONITE,
        0x46: DODUO,
        0x47: POLIWAG,
        0x48: JYNX,
        0x49: MOLTRES,
        0x4A: ARTICUNO,
        0x4B: ZAPDOS,
        0x4C: DITTO,
        0x4D: MEOWTH,
        0x4E: KRABBY,
        0x52: VULPIX,
        0x53: NINETALES,
        0x54: PIKACHU,
        0x55: RAICHU,
        0x58: DRATINI,
        0x59: DRAGONAIR,
        0x5A: KABUTO,
        0x5B: KABUTOPS,
        0x5C: HORSEA,
        0x5D: SEADRA,
        0x60: SANDSHREW,
        0x61: SANDSLASH,
        0x62: OMANYTE,
        0x63: OMASTAR,
        0x64: JIGGLYPUFF,
        0x65: WIGGLYTUFF,
        0x66: EEVEE,
        0x67: FLAREON,
        0x68: JOLTEON,
        0x69: VAPOREON,
        0x6A: MACHOP,
        0x6B: ZUBAT,
        0x6C: EKANS,
        0x6D: PARAS,
        0x6E: POLIWHIRL,
        0x6F: POLIWRATH,
        0x70: WEEDLE,
        0x71: KAKUNA,
        0x72: BEEDRILL,
        0x74: DODRIO,
        0x75: PRIMEAPE,
        0x76: DUGTRIO,
        0x77: VENOMOTH,
        0x78: DEWGONG,
        0x7B: CATERPIE,
        0x7C: METAPOD,
        0x7D: BUTTERFREE,
        0x7E: MACHAMP,
        0x80: GOLDUCK,
        0x81: HYPNO,
        0x82: GOLBAT,
        0x83: MEWTWO,
        0x84: SNORLAX,
        0x85: MAGIKARP,
        0x88: MUK,
        0x8A: KINGLER,
        0x8B: CLOYSTER,
        0x8D: ELECTRODE,
        0x8E: CLEFABLE,
        0x8F: WEEZING,
        0x90: PERSIAN,
        0x91: MAROWAK,
        0x93: HAUNTER,
        0x94: ABRA,
        0x95: ALAKAZAM,
        0x96: PIDGEOTTO,
        0x97: PIDGEOT,
        0x98: STARMIE,
        0x99: BULBASAUR,
        0x9A: VENUSAUR,
        0x9B: TENTACRUEL,
        0x9D: GOLDEEN,
        0x9E: SEAKING,
        0xA3: PONYTA,
        0xA4: RAPIDASH,
        0xA5: RATTATA,
        0xA6: RATICATE,
        0xA7: NIDORINO,
        0xA8: NIDORINA,
        0xA9: GEODUDE,
        0xAA: PORYGON,
        0xAB: AERODACTYL,
        0xAD: MAGNEMITE,
        0xB0: CHARMANDER,
        0xB1: SQUIRTLE,
        0xB2: CHARMELEON,
        0xB3: WARTORTLE,
        0xB4: CHARIZARD,
        0xB9: ODDISH,
        0xBA: GLOOM,
        0xBB: VILEPLUME,
        0xBC: BELLSPROUT,
        0xBD: WEEPINBELL,
        0xBE: VICTREEBEL,
    }
)

#: International version RAM address to meaning (reversible)
INTL_BYTE_TO_MEANING = bidict(
    {
        0xD2F7: OWN_1_8,
        0xD2F8: OWN_9_16,
        0xD2F9: OWN_17_24,
        0xD2FA: OWN_25_32,
        0xD2FB: OWN_33_40,
        0xD2FC: OWN_41_48,
        0xD2FD: OWN_49_56,
        0xD2FE: OWN_57_64,
        0xD2FF: OWN_65_72,
        0xD300: OWN_73_80,
        0xD301: OWN_81_88,
        0xD302: OWN_89_96,
        0xD303: OWN_97_104,
        0xD304: OWN_105_112,
        0xD305: OWN_113_120,
        0xD306: OWN_121_128,
        0xD307: OWN_129_136,
        0xD308: OWN_137_144,
        0xD309: OWN_145_152,
        0xD30A: SEEN_1_8,
        0xD30B: SEEN_9_16,
        0xD30C: SEEN_17_24,
        0xD30D: SEEN_25_32,
        0xD30E: SEEN_33_40,
        0xD30F: SEEN_41_48,
        0xD310: SEEN_49_56,
        0xD311: SEEN_57_64,
        0xD312: SEEN_65_72,
        0xD313: SEEN_73_80,
        0xD314: SEEN_81_88,
        0xD315: SEEN_89_96,
        0xD316: SEEN_97_104,
        0xD317: SEEN_105_112,
        0xD318: SEEN_113_120,
        0xD319: SEEN_121_128,
        0xD31A: SEEN_129_136,
        0xD31B: SEEN_137_144,
        0xD31C: SEEN_145_152,
    }
)

#: International version RAM address and bit to meaning
INTL_BIT_TO_MEANING = {
    0xD2F7: {
        0: RHYDON_OWNED,
        1: KANGASKHAN_OWNED,
        2: NIDORAN_M_OWNED,
        3: CLEFAIRY_OWNED,
        4: SPEAROW_OWNED,
        5: VOLTORB_OWNED,
        6: NIDOKING_OWNED,
        7: SLOWBRO_OWNED,
    },
    0xD2F8: {
        0: IVYSAUR_OWNED,
        1: EXEGGUTOR_OWNED,
        2: LICKITUNG_OWNED,
        3: EXEGGCUTE_OWNED,
        4: GRIMER_OWNED,
        5: GENGAR_OWNED,
        6: NIDORAN_F_OWNED,
        7: NIDOQUEEN_OWNED,
    },
    0xD2F9: {
        0: CUBONE_OWNED,
        1: RHYHORN_OWNED,
        2: LAPRAS_OWNED,
        3: ARCANINE_OWNED,
        4: MEW_OWNED,
        5: GYARADOS_OWNED,
        6: SHELLDER_OWNED,
        7: TENTACOOL_OWNED,
    },
    0xD2FA: {
        0: GASTLY_OWNED,
        1: SCYTHER_OWNED,
        2: STARYU_OWNED,
        3: BLASTOISE_OWNED,
        4: PINSIR_OWNED,
        5: TANGELA_OWNED,
        6: GROWLITHE_OWNED,
        7: ONIX_OWNED,
    },
    0xD2FB: {
        0: FEAROW_OWNED,
        1: PIDGEY_OWNED,
        2: SLOWPOKE_OWNED,
        3: KADABRA_OWNED,
        4: GRAVELER_OWNED,
        5: CHANSEY_OWNED,
        6: MACHOKE_OWNED,
        7: MRMIME_OWNED,
    },
    0xD2FC: {
        0: HITMONLEE_OWNED,
        1: HITMONCHAN_OWNED,
        2: ARBOK_OWNED,
        3: PARASECT_OWNED,
        4: PSYDUCK_OWNED,
        5: DROWZEE_OWNED,
        6: GOLEM_OWNED,
        7: MAGMAR_OWNED,
    },
    0xD2FD: {
        0: ELECTABUZZ_OWNED,
        1: MAGNETON_OWNED,
        2: KOFFING_OWNED,
        3: MANKEY_OWNED,
        4: SEEL_OWNED,
        5: DIGLETT_OWNED,
        6: TAUROS_OWNED,
        7: FARFETCHD_OWNED,
    },
    0xD2FE: {
        0: VENONAT_OWNED,
        1: DRAGONITE_OWNED,
        2: DODUO_OWNED,
        3: POLIWAG_OWNED,
        4: JYNX_OWNED,
        5: MOLTRES_OWNED,
        6: ARTICUNO_OWNED,
        7: ZAPDOS_OWNED,
    },
    0xD2FF: {
        0: DITTO_OWNED,
        1: MEOWTH_OWNED,
        2: KRABBY_OWNED,
        3: VULPIX_OWNED,
        4: NINETALES_OWNED,
        5: PIKACHU_OWNED,
        6: RAICHU_OWNED,
        7: DRATINI_OWNED,
    },
    0xD300: {
        0: DRAGONAIR_OWNED,
        1: KABUTO_OWNED,
        2: KABUTOPS_OWNED,
        3: HORSEA_OWNED,
        4: SEADRA_OWNED,
        5: SANDSHREW_OWNED,
        6: SANDSLASH_OWNED,
        7: OMANYTE_OWNED,
    },
    0xD301: {
        0: OMASTAR_OWNED,
        1: JIGGLYPUFF_OWNED,
        2: WIGGLYTUFF_OWNED,
        3: EEVEE_OWNED,
        4: FLAREON_OWNED,
        5: JOLTEON_OWNED,
        6: VAPOREON_OWNED,
        7: MACHOP_OWNED,
    },
    0xD302: {
        0: ZUBAT_OWNED,
        1: EKANS_OWNED,
        2: PARAS_OWNED,
        3: POLIWHIRL_OWNED,
        4: POLIWRATH_OWNED,
        5: WEEDLE_OWNED,
        6: KAKUNA_OWNED,
        7: BEEDRILL_OWNED,
    },
    0xD303: {
        0: DODRIO_OWNED,
        1: PRIMEAPE_OWNED,
        2: DUGTRIO_OWNED,
        3: VENOMOTH_OWNED,
        4: DEWGONG_OWNED,
        5: CATERPIE_OWNED,
        6: METAPOD_OWNED,
        7: BUTTERFREE_OWNED,
    },
    0xD304: {
        0: MACHAMP_OWNED,
        1: GOLDUCK_OWNED,
        2: HYPNO_OWNED,
        3: GOLBAT_OWNED,
        4: MEWTWO_OWNED,
        5: SNORLAX_OWNED,
        6: MAGIKARP_OWNED,
        7: MUK_OWNED,
    },
    0xD305: {
        0: KINGLER_OWNED,
        1: CLOYSTER_OWNED,
        2: ELECTRODE_OWNED,
        3: CLEFABLE_OWNED,
        4: WEEZING_OWNED,
        5: PERSIAN_OWNED,
        6: MAROWAK_OWNED,
        7: HAUNTER_OWNED,
    },
    0xD306: {
        0: ABRA_OWNED,
        1: ALAKAZAM_OWNED,
        2: PIDGEOTTO_OWNED,
        3: PIDGEOT_OWNED,
        4: STARMIE_OWNED,
        5: BULBASAUR_OWNED,
        6: VENUSAUR_OWNED,
        7: TENTACRUEL_OWNED,
    },
    0xD307: {
        0: GOLDEEN_OWNED,
        1: SEAKING_OWNED,
        2: PONYTA_OWNED,
        3: RAPIDASH_OWNED,
        4: RATTATA_OWNED,
        5: RATICATE_OWNED,
        6: NIDORINO_OWNED,
        7: NIDORINA_OWNED,
    },
    0xD308: {
        0: GEODUDE_OWNED,
        1: PORYGON_OWNED,
        2: AERODACTYL_OWNED,
        3: MAGNEMITE_OWNED,
        4: CHARMANDER_OWNED,
        5: SQUIRTLE_OWNED,
        6: CHARMELEON_OWNED,
        7: WARTORTLE_OWNED,
    },
    0xD309: {
        0: CHARIZARD_OWNED,
        1: ODDISH_OWNED,
        2: GLOOM_OWNED,
        3: VILEPLUME_OWNED,
        4: BELLSPROUT_OWNED,
        5: WEEPINBELL_OWNED,
        6: VICTREEBEL_OWNED,
    },
    0xD30A: {
        0: RHYDON_SEEN,
        1: KANGASKHAN_SEEN,
        2: NIDORAN_M_SEEN,
        3: CLEFAIRY_SEEN,
        4: SPEAROW_SEEN,
        5: VOLTORB_SEEN,
        6: NIDOKING_SEEN,
        7: SLOWBRO_SEEN,
    },
    0xD30B: {
        0: IVYSAUR_SEEN,
        1: EXEGGUTOR_SEEN,
        2: LICKITUNG_SEEN,
        3: EXEGGCUTE_SEEN,
        4: GRIMER_SEEN,
        5: GENGAR_SEEN,
        6: NIDORAN_F_SEEN,
        7: NIDOQUEEN_SEEN,
    },
    0xD30C: {
        0: CUBONE_SEEN,
        1: RHYHORN_SEEN,
        2: LAPRAS_SEEN,
        3: ARCANINE_SEEN,
        4: MEW_SEEN,
        5: GYARADOS_SEEN,
        6: SHELLDER_SEEN,
        7: TENTACOOL_SEEN,
    },
    0xD30D: {
        0: GASTLY_SEEN,
        1: SCYTHER_SEEN,
        2: STARYU_SEEN,
        3: BLASTOISE_SEEN,
        4: PINSIR_SEEN,
        5: TANGELA_SEEN,
        6: GROWLITHE_SEEN,
        7: ONIX_SEEN,
    },
    0xD30E: {
        0: FEAROW_SEEN,
        1: PIDGEY_SEEN,
        2: SLOWPOKE_SEEN,
        3: KADABRA_SEEN,
        4: GRAVELER_SEEN,
        5: CHANSEY_SEEN,
        6: MACHOKE_SEEN,
        7: MRMIME_SEEN,
    },
    0xD30F: {
        0: HITMONLEE_SEEN,
        1: HITMONCHAN_SEEN,
        2: ARBOK_SEEN,
        3: PARASECT_SEEN,
        4: PSYDUCK_SEEN,
        5: DROWZEE_SEEN,
        6: GOLEM_SEEN,
        7: MAGMAR_SEEN,
    },
    0xD310: {
        0: ELECTABUZZ_SEEN,
        1: MAGNETON_SEEN,
        2: KOFFING_SEEN,
        3: MANKEY_SEEN,
        4: SEEL_SEEN,
        5: DIGLETT_SEEN,
        6: TAUROS_SEEN,
        7: FARFETCHD_SEEN,
    },
    0xD311: {
        0: VENONAT_SEEN,
        1: DRAGONITE_SEEN,
        2: DODUO_SEEN,
        3: POLIWAG_SEEN,
        4: JYNX_SEEN,
        5: MOLTRES_SEEN,
        6: ARTICUNO_SEEN,
        7: ZAPDOS_SEEN,
    },
    0xD312: {
        0: DITTO_SEEN,
        1: MEOWTH_SEEN,
        2: KRABBY_SEEN,
        3: VULPIX_SEEN,
        4: NINETALES_SEEN,
        5: PIKACHU_SEEN,
        6: RAICHU_SEEN,
        7: DRATINI_SEEN,
    },
    0xD313: {
        0: DRAGONAIR_SEEN,
        1: KABUTO_SEEN,
        2: KABUTOPS_SEEN,
        3: HORSEA_SEEN,
        4: SEADRA_SEEN,
        5: SANDSHREW_SEEN,
        6: SANDSLASH_SEEN,
        7: OMANYTE_SEEN,
    },
    0xD314: {
        0: OMASTAR_SEEN,
        1: JIGGLYPUFF_SEEN,
        2: WIGGLYTUFF_SEEN,
        3: EEVEE_SEEN,
        4: FLAREON_SEEN,
        5: JOLTEON_SEEN,
        6: VAPOREON_SEEN,
        7: MACHOP_SEEN,
    },
    0xD315: {
        0: ZUBAT_SEEN,
        1: EKANS_SEEN,
        2: PARAS_SEEN,
        3: POLIWHIRL_SEEN,
        4: POLIWRATH_SEEN,
        5: WEEDLE_SEEN,
        6: KAKUNA_SEEN,
        7: BEEDRILL_SEEN,
    },
    0xD316: {
        0: DODRIO_SEEN,
        1: PRIMEAPE_SEEN,
        2: DUGTRIO_SEEN,
        3: VENOMOTH_SEEN,
        4: DEWGONG_SEEN,
        5: CATERPIE_SEEN,
        6: METAPOD_SEEN,
        7: BUTTERFREE_SEEN,
    },
    0xD317: {
        0: MACHAMP_SEEN,
        1: GOLDUCK_SEEN,
        2: HYPNO_SEEN,
        3: GOLBAT_SEEN,
        4: MEWTWO_SEEN,
        5: SNORLAX_SEEN,
        6: MAGIKARP_SEEN,
        7: MUK_SEEN,
    },
    0xD318: {
        0: KINGLER_SEEN,
        1: CLOYSTER_SEEN,
        2: ELECTRODE_SEEN,
        3: CLEFABLE_SEEN,
        4: WEEZING_SEEN,
        5: PERSIAN_SEEN,
        6: MAROWAK_SEEN,
        7: HAUNTER_SEEN,
    },
    0xD319: {
        0: ABRA_SEEN,
        1: ALAKAZAM_SEEN,
        2: PIDGEOTTO_SEEN,
        3: PIDGEOT_SEEN,
        4: STARMIE_SEEN,
        5: BULBASAUR_SEEN,
        6: VENUSAUR_SEEN,
        7: TENTACRUEL_SEEN,
    },
    0xD31A: {
        0: GOLDEEN_SEEN,
        1: SEAKING_SEEN,
        2: PONYTA_SEEN,
        3: RAPIDASH_SEEN,
        4: RATTATA_SEEN,
        5: RATICATE_SEEN,
        6: NIDORINO_SEEN,
        7: NIDORINA_SEEN,
    },
    0xD31B: {
        0: GEODUDE_SEEN,
        1: PORYGON_SEEN,
        2: AERODACTYL_SEEN,
        3: MAGNEMITE_SEEN,
        4: CHARMANDER_SEEN,
        5: SQUIRTLE_SEEN,
        6: CHARMELEON_SEEN,
        7: WARTORTLE_SEEN,
    },
    0xD31C: {
        0: CHARIZARD_SEEN,
        1: ODDISH_SEEN,
        2: GLOOM_SEEN,
        3: VILEPLUME_SEEN,
        4: BELLSPROUT_SEEN,
        5: WEEPINBELL_SEEN,
        6: VICTREEBEL_SEEN,
    },
}

#: International version bit-value meaning to byte address and bit
INTL_MEANING_TO_BIT = {}
for address, values in INTL_BIT_TO_MEANING.items():
    for bit, meaning in values.items():
        INTL_MEANING_TO_BIT[meaning] = (address, bit)


class PokemonRedBlueInfo(CartridgeInfo):
    @staticmethod
    def byte_for_meaning(meaning: str) -> int:
        """
        Get the address corresponding to a specific meaning for a given
        cartridge.

        If the meaning corresponds to a single bit within a byte, return the
        address of that byte

        Raises
        ------
        ValueError
            If the meaning doesn't apply to this cartridge
        """

        if meaning in INTL_BYTE_TO_MEANING.inverse:
            return INTL_BYTE_TO_MEANING.inverse[meaning]

        if meaning in INTL_MEANING_TO_BIT:
            address, bit = INTL_MEANING_TO_BIT[meaning]
            return address

        raise ValueError(f"No address for {meaning!r}")

    @staticmethod
    def meaning_for_byte_change(
        address: int,
        old_value: Optional[int],
        new_value: int,
    ) -> List[ChangeMeaning]:
        """
        Meanings corresponding to a change in byte value from one to another.

        The return value is a list of tuples containing the meaning of the
        change, and whether it's a positive or negative result
        """

        if address in INTL_BIT_TO_MEANING:
            new_bits = [int(i) for i in "{0:08b}".format(new_value)]
            old_bits = (
                [int(i) for i in "{0:08b}".format(old_value)]
                if old_value is not None
                else [not i for i in new_bits]
            )
            changed_bits = [
                location
                for location in range(len(new_bits))
                if new_bits[location] != old_bits[location]
            ]

            results = []
            for change in changed_bits:
                try:
                    meaning = INTL_BIT_TO_MEANING[address][change]
                except KeyError:
                    continue
                positive = new_bits[change] == 1
                results.append(ChangeMeaning(meaning=meaning, value=positive))

            return results

        if address in INTL_BYTE_TO_MEANING:
            # TODO: Refactor to have proper values parsing
            return [ChangeMeaning(meaning=INTL_BYTE_TO_MEANING[address], value=True)]

        return []
