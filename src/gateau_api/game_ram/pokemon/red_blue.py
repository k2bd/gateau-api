from typing import List, Optional

from bidict import bidict

from gateau_api.game_ram.cartridge_info import CartridgeInfo, ChangeMeaning

from . import constants

#: Internal ID to Pokemon (reversible)
ID_TO_POKEMON = bidict(
    {
        0x1: constants.RHYDON,
        0x2: constants.KANGASKHAN,
        0x3: constants.NIDORAN_M,
        0x4: constants.CLEFAIRY,
        0x5: constants.SPEAROW,
        0x6: constants.VOLTORB,
        0x7: constants.NIDOKING,
        0x8: constants.SLOWBRO,
        0x9: constants.IVYSAUR,
        0x0A: constants.EXEGGUTOR,
        0x0B: constants.LICKITUNG,
        0x0C: constants.EXEGGCUTE,
        0x0D: constants.GRIMER,
        0x0E: constants.GENGAR,
        0x0F: constants.NIDORAN_F,
        0x10: constants.NIDOQUEEN,
        0x11: constants.CUBONE,
        0x12: constants.RHYHORN,
        0x13: constants.LAPRAS,
        0x14: constants.ARCANINE,
        0x15: constants.MEW,
        0x16: constants.GYARADOS,
        0x17: constants.SHELLDER,
        0x18: constants.TENTACOOL,
        0x19: constants.GASTLY,
        0x1A: constants.SCYTHER,
        0x1B: constants.STARYU,
        0x1C: constants.BLASTOISE,
        0x1D: constants.PINSIR,
        0x1E: constants.TANGELA,
        0x21: constants.GROWLITHE,
        0x22: constants.ONIX,
        0x23: constants.FEAROW,
        0x24: constants.PIDGEY,
        0x25: constants.SLOWPOKE,
        0x26: constants.KADABRA,
        0x27: constants.GRAVELER,
        0x28: constants.CHANSEY,
        0x29: constants.MACHOKE,
        0x2A: constants.MRMIME,
        0x2B: constants.HITMONLEE,
        0x2C: constants.HITMONCHAN,
        0x2D: constants.ARBOK,
        0x2E: constants.PARASECT,
        0x2F: constants.PSYDUCK,
        0x30: constants.DROWZEE,
        0x31: constants.GOLEM,
        0x33: constants.MAGMAR,
        0x35: constants.ELECTABUZZ,
        0x36: constants.MAGNETON,
        0x37: constants.KOFFING,
        0x39: constants.MANKEY,
        0x3A: constants.SEEL,
        0x3B: constants.DIGLETT,
        0x3C: constants.TAUROS,
        0x40: constants.FARFETCHD,
        0x41: constants.VENONAT,
        0x42: constants.DRAGONITE,
        0x46: constants.DODUO,
        0x47: constants.POLIWAG,
        0x48: constants.JYNX,
        0x49: constants.MOLTRES,
        0x4A: constants.ARTICUNO,
        0x4B: constants.ZAPDOS,
        0x4C: constants.DITTO,
        0x4D: constants.MEOWTH,
        0x4E: constants.KRABBY,
        0x52: constants.VULPIX,
        0x53: constants.NINETALES,
        0x54: constants.PIKACHU,
        0x55: constants.RAICHU,
        0x58: constants.DRATINI,
        0x59: constants.DRAGONAIR,
        0x5A: constants.KABUTO,
        0x5B: constants.KABUTOPS,
        0x5C: constants.HORSEA,
        0x5D: constants.SEADRA,
        0x60: constants.SANDSHREW,
        0x61: constants.SANDSLASH,
        0x62: constants.OMANYTE,
        0x63: constants.OMASTAR,
        0x64: constants.JIGGLYPUFF,
        0x65: constants.WIGGLYTUFF,
        0x66: constants.EEVEE,
        0x67: constants.FLAREON,
        0x68: constants.JOLTEON,
        0x69: constants.VAPOREON,
        0x6A: constants.MACHOP,
        0x6B: constants.ZUBAT,
        0x6C: constants.EKANS,
        0x6D: constants.PARAS,
        0x6E: constants.POLIWHIRL,
        0x6F: constants.POLIWRATH,
        0x70: constants.WEEDLE,
        0x71: constants.KAKUNA,
        0x72: constants.BEEDRILL,
        0x74: constants.DODRIO,
        0x75: constants.PRIMEAPE,
        0x76: constants.DUGTRIO,
        0x77: constants.VENOMOTH,
        0x78: constants.DEWGONG,
        0x7B: constants.CATERPIE,
        0x7C: constants.METAPOD,
        0x7D: constants.BUTTERFREE,
        0x7E: constants.MACHAMP,
        0x80: constants.GOLDUCK,
        0x81: constants.HYPNO,
        0x82: constants.GOLBAT,
        0x83: constants.MEWTWO,
        0x84: constants.SNORLAX,
        0x85: constants.MAGIKARP,
        0x88: constants.MUK,
        0x8A: constants.KINGLER,
        0x8B: constants.CLOYSTER,
        0x8D: constants.ELECTRODE,
        0x8E: constants.CLEFABLE,
        0x8F: constants.WEEZING,
        0x90: constants.PERSIAN,
        0x91: constants.MAROWAK,
        0x93: constants.HAUNTER,
        0x94: constants.ABRA,
        0x95: constants.ALAKAZAM,
        0x96: constants.PIDGEOTTO,
        0x97: constants.PIDGEOT,
        0x98: constants.STARMIE,
        0x99: constants.BULBASAUR,
        0x9A: constants.VENUSAUR,
        0x9B: constants.TENTACRUEL,
        0x9D: constants.GOLDEEN,
        0x9E: constants.SEAKING,
        0xA3: constants.PONYTA,
        0xA4: constants.RAPIDASH,
        0xA5: constants.RATTATA,
        0xA6: constants.RATICATE,
        0xA7: constants.NIDORINO,
        0xA8: constants.NIDORINA,
        0xA9: constants.GEODUDE,
        0xAA: constants.PORYGON,
        0xAB: constants.AERODACTYL,
        0xAD: constants.MAGNEMITE,
        0xB0: constants.CHARMANDER,
        0xB1: constants.SQUIRTLE,
        0xB2: constants.CHARMELEON,
        0xB3: constants.WARTORTLE,
        0xB4: constants.CHARIZARD,
        0xB9: constants.ODDISH,
        0xBA: constants.GLOOM,
        0xBB: constants.VILEPLUME,
        0xBC: constants.BELLSPROUT,
        0xBD: constants.WEEPINBELL,
        0xBE: constants.VICTREEBEL,
    }
)

#: International version RAM address to meaning (reversible)
INTL_BYTE_TO_MEANING = bidict(
    {
        0xD2F7: constants.OWN_1_8,
        0xD2F8: constants.OWN_9_16,
        0xD2F9: constants.OWN_17_24,
        0xD2FA: constants.OWN_25_32,
        0xD2FB: constants.OWN_33_40,
        0xD2FC: constants.OWN_41_48,
        0xD2FD: constants.OWN_49_56,
        0xD2FE: constants.OWN_57_64,
        0xD2FF: constants.OWN_65_72,
        0xD300: constants.OWN_73_80,
        0xD301: constants.OWN_81_88,
        0xD302: constants.OWN_89_96,
        0xD303: constants.OWN_97_104,
        0xD304: constants.OWN_105_112,
        0xD305: constants.OWN_113_120,
        0xD306: constants.OWN_121_128,
        0xD307: constants.OWN_129_136,
        0xD308: constants.OWN_137_144,
        0xD309: constants.OWN_145_152,
        0xD30A: constants.SEEN_1_8,
        0xD30B: constants.SEEN_9_16,
        0xD30C: constants.SEEN_17_24,
        0xD30D: constants.SEEN_25_32,
        0xD30E: constants.SEEN_33_40,
        0xD30F: constants.SEEN_41_48,
        0xD310: constants.SEEN_49_56,
        0xD311: constants.SEEN_57_64,
        0xD312: constants.SEEN_65_72,
        0xD313: constants.SEEN_73_80,
        0xD314: constants.SEEN_81_88,
        0xD315: constants.SEEN_89_96,
        0xD316: constants.SEEN_97_104,
        0xD317: constants.SEEN_105_112,
        0xD318: constants.SEEN_113_120,
        0xD319: constants.SEEN_121_128,
        0xD31A: constants.SEEN_129_136,
        0xD31B: constants.SEEN_137_144,
        0xD31C: constants.SEEN_145_152,
    }
)

#: International version RAM address and bit to meaning
INTL_BIT_TO_MEANING = {
    0xD2F7: {
        0: constants.RHYDON_OWNED,
        1: constants.KANGASKHAN_OWNED,
        2: constants.NIDORAN_M_OWNED,
        3: constants.CLEFAIRY_OWNED,
        4: constants.SPEAROW_OWNED,
        5: constants.VOLTORB_OWNED,
        6: constants.NIDOKING_OWNED,
        7: constants.SLOWBRO_OWNED,
    },
    0xD2F8: {
        0: constants.IVYSAUR_OWNED,
        1: constants.EXEGGUTOR_OWNED,
        2: constants.LICKITUNG_OWNED,
        3: constants.EXEGGCUTE_OWNED,
        4: constants.GRIMER_OWNED,
        5: constants.GENGAR_OWNED,
        6: constants.NIDORAN_F_OWNED,
        7: constants.NIDOQUEEN_OWNED,
    },
    0xD2F9: {
        0: constants.CUBONE_OWNED,
        1: constants.RHYHORN_OWNED,
        2: constants.LAPRAS_OWNED,
        3: constants.ARCANINE_OWNED,
        4: constants.MEW_OWNED,
        5: constants.GYARADOS_OWNED,
        6: constants.SHELLDER_OWNED,
        7: constants.TENTACOOL_OWNED,
    },
    0xD2FA: {
        0: constants.GASTLY_OWNED,
        1: constants.SCYTHER_OWNED,
        2: constants.STARYU_OWNED,
        3: constants.BLASTOISE_OWNED,
        4: constants.PINSIR_OWNED,
        5: constants.TANGELA_OWNED,
        6: constants.GROWLITHE_OWNED,
        7: constants.ONIX_OWNED,
    },
    0xD2FB: {
        0: constants.FEAROW_OWNED,
        1: constants.PIDGEY_OWNED,
        2: constants.SLOWPOKE_OWNED,
        3: constants.KADABRA_OWNED,
        4: constants.GRAVELER_OWNED,
        5: constants.CHANSEY_OWNED,
        6: constants.MACHOKE_OWNED,
        7: constants.MRMIME_OWNED,
    },
    0xD2FC: {
        0: constants.HITMONLEE_OWNED,
        1: constants.HITMONCHAN_OWNED,
        2: constants.ARBOK_OWNED,
        3: constants.PARASECT_OWNED,
        4: constants.PSYDUCK_OWNED,
        5: constants.DROWZEE_OWNED,
        6: constants.GOLEM_OWNED,
        7: constants.MAGMAR_OWNED,
    },
    0xD2FD: {
        0: constants.ELECTABUZZ_OWNED,
        1: constants.MAGNETON_OWNED,
        2: constants.KOFFING_OWNED,
        3: constants.MANKEY_OWNED,
        4: constants.SEEL_OWNED,
        5: constants.DIGLETT_OWNED,
        6: constants.TAUROS_OWNED,
        7: constants.FARFETCHD_OWNED,
    },
    0xD2FE: {
        0: constants.VENONAT_OWNED,
        1: constants.DRAGONITE_OWNED,
        2: constants.DODUO_OWNED,
        3: constants.POLIWAG_OWNED,
        4: constants.JYNX_OWNED,
        5: constants.MOLTRES_OWNED,
        6: constants.ARTICUNO_OWNED,
        7: constants.ZAPDOS_OWNED,
    },
    0xD2FF: {
        0: constants.DITTO_OWNED,
        1: constants.MEOWTH_OWNED,
        2: constants.KRABBY_OWNED,
        3: constants.VULPIX_OWNED,
        4: constants.NINETALES_OWNED,
        5: constants.PIKACHU_OWNED,
        6: constants.RAICHU_OWNED,
        7: constants.DRATINI_OWNED,
    },
    0xD300: {
        0: constants.DRAGONAIR_OWNED,
        1: constants.KABUTO_OWNED,
        2: constants.KABUTOPS_OWNED,
        3: constants.HORSEA_OWNED,
        4: constants.SEADRA_OWNED,
        5: constants.SANDSHREW_OWNED,
        6: constants.SANDSLASH_OWNED,
        7: constants.OMANYTE_OWNED,
    },
    0xD301: {
        0: constants.OMASTAR_OWNED,
        1: constants.JIGGLYPUFF_OWNED,
        2: constants.WIGGLYTUFF_OWNED,
        3: constants.EEVEE_OWNED,
        4: constants.FLAREON_OWNED,
        5: constants.JOLTEON_OWNED,
        6: constants.VAPOREON_OWNED,
        7: constants.MACHOP_OWNED,
    },
    0xD302: {
        0: constants.ZUBAT_OWNED,
        1: constants.EKANS_OWNED,
        2: constants.PARAS_OWNED,
        3: constants.POLIWHIRL_OWNED,
        4: constants.POLIWRATH_OWNED,
        5: constants.WEEDLE_OWNED,
        6: constants.KAKUNA_OWNED,
        7: constants.BEEDRILL_OWNED,
    },
    0xD303: {
        0: constants.DODRIO_OWNED,
        1: constants.PRIMEAPE_OWNED,
        2: constants.DUGTRIO_OWNED,
        3: constants.VENOMOTH_OWNED,
        4: constants.DEWGONG_OWNED,
        5: constants.CATERPIE_OWNED,
        6: constants.METAPOD_OWNED,
        7: constants.BUTTERFREE_OWNED,
    },
    0xD304: {
        0: constants.MACHAMP_OWNED,
        1: constants.GOLDUCK_OWNED,
        2: constants.HYPNO_OWNED,
        3: constants.GOLBAT_OWNED,
        4: constants.MEWTWO_OWNED,
        5: constants.SNORLAX_OWNED,
        6: constants.MAGIKARP_OWNED,
        7: constants.MUK_OWNED,
    },
    0xD305: {
        0: constants.KINGLER_OWNED,
        1: constants.CLOYSTER_OWNED,
        2: constants.ELECTRODE_OWNED,
        3: constants.CLEFABLE_OWNED,
        4: constants.WEEZING_OWNED,
        5: constants.PERSIAN_OWNED,
        6: constants.MAROWAK_OWNED,
        7: constants.HAUNTER_OWNED,
    },
    0xD306: {
        0: constants.ABRA_OWNED,
        1: constants.ALAKAZAM_OWNED,
        2: constants.PIDGEOTTO_OWNED,
        3: constants.PIDGEOT_OWNED,
        4: constants.STARMIE_OWNED,
        5: constants.BULBASAUR_OWNED,
        6: constants.VENUSAUR_OWNED,
        7: constants.TENTACRUEL_OWNED,
    },
    0xD307: {
        0: constants.GOLDEEN_OWNED,
        1: constants.SEAKING_OWNED,
        2: constants.PONYTA_OWNED,
        3: constants.RAPIDASH_OWNED,
        4: constants.RATTATA_OWNED,
        5: constants.RATICATE_OWNED,
        6: constants.NIDORINO_OWNED,
        7: constants.NIDORINA_OWNED,
    },
    0xD308: {
        0: constants.GEODUDE_OWNED,
        1: constants.PORYGON_OWNED,
        2: constants.AERODACTYL_OWNED,
        3: constants.MAGNEMITE_OWNED,
        4: constants.CHARMANDER_OWNED,
        5: constants.SQUIRTLE_OWNED,
        6: constants.CHARMELEON_OWNED,
        7: constants.WARTORTLE_OWNED,
    },
    0xD309: {
        0: constants.CHARIZARD_OWNED,
        1: constants.ODDISH_OWNED,
        2: constants.GLOOM_OWNED,
        3: constants.VILEPLUME_OWNED,
        4: constants.BELLSPROUT_OWNED,
        5: constants.WEEPINBELL_OWNED,
        6: constants.VICTREEBEL_OWNED,
    },
    0xD30A: {
        0: constants.RHYDON_SEEN,
        1: constants.KANGASKHAN_SEEN,
        2: constants.NIDORAN_M_SEEN,
        3: constants.CLEFAIRY_SEEN,
        4: constants.SPEAROW_SEEN,
        5: constants.VOLTORB_SEEN,
        6: constants.NIDOKING_SEEN,
        7: constants.SLOWBRO_SEEN,
    },
    0xD30B: {
        0: constants.IVYSAUR_SEEN,
        1: constants.EXEGGUTOR_SEEN,
        2: constants.LICKITUNG_SEEN,
        3: constants.EXEGGCUTE_SEEN,
        4: constants.GRIMER_SEEN,
        5: constants.GENGAR_SEEN,
        6: constants.NIDORAN_F_SEEN,
        7: constants.NIDOQUEEN_SEEN,
    },
    0xD30C: {
        0: constants.CUBONE_SEEN,
        1: constants.RHYHORN_SEEN,
        2: constants.LAPRAS_SEEN,
        3: constants.ARCANINE_SEEN,
        4: constants.MEW_SEEN,
        5: constants.GYARADOS_SEEN,
        6: constants.SHELLDER_SEEN,
        7: constants.TENTACOOL_SEEN,
    },
    0xD30D: {
        0: constants.GASTLY_SEEN,
        1: constants.SCYTHER_SEEN,
        2: constants.STARYU_SEEN,
        3: constants.BLASTOISE_SEEN,
        4: constants.PINSIR_SEEN,
        5: constants.TANGELA_SEEN,
        6: constants.GROWLITHE_SEEN,
        7: constants.ONIX_SEEN,
    },
    0xD30E: {
        0: constants.FEAROW_SEEN,
        1: constants.PIDGEY_SEEN,
        2: constants.SLOWPOKE_SEEN,
        3: constants.KADABRA_SEEN,
        4: constants.GRAVELER_SEEN,
        5: constants.CHANSEY_SEEN,
        6: constants.MACHOKE_SEEN,
        7: constants.MRMIME_SEEN,
    },
    0xD30F: {
        0: constants.HITMONLEE_SEEN,
        1: constants.HITMONCHAN_SEEN,
        2: constants.ARBOK_SEEN,
        3: constants.PARASECT_SEEN,
        4: constants.PSYDUCK_SEEN,
        5: constants.DROWZEE_SEEN,
        6: constants.GOLEM_SEEN,
        7: constants.MAGMAR_SEEN,
    },
    0xD310: {
        0: constants.ELECTABUZZ_SEEN,
        1: constants.MAGNETON_SEEN,
        2: constants.KOFFING_SEEN,
        3: constants.MANKEY_SEEN,
        4: constants.SEEL_SEEN,
        5: constants.DIGLETT_SEEN,
        6: constants.TAUROS_SEEN,
        7: constants.FARFETCHD_SEEN,
    },
    0xD311: {
        0: constants.VENONAT_SEEN,
        1: constants.DRAGONITE_SEEN,
        2: constants.DODUO_SEEN,
        3: constants.POLIWAG_SEEN,
        4: constants.JYNX_SEEN,
        5: constants.MOLTRES_SEEN,
        6: constants.ARTICUNO_SEEN,
        7: constants.ZAPDOS_SEEN,
    },
    0xD312: {
        0: constants.DITTO_SEEN,
        1: constants.MEOWTH_SEEN,
        2: constants.KRABBY_SEEN,
        3: constants.VULPIX_SEEN,
        4: constants.NINETALES_SEEN,
        5: constants.PIKACHU_SEEN,
        6: constants.RAICHU_SEEN,
        7: constants.DRATINI_SEEN,
    },
    0xD313: {
        0: constants.DRAGONAIR_SEEN,
        1: constants.KABUTO_SEEN,
        2: constants.KABUTOPS_SEEN,
        3: constants.HORSEA_SEEN,
        4: constants.SEADRA_SEEN,
        5: constants.SANDSHREW_SEEN,
        6: constants.SANDSLASH_SEEN,
        7: constants.OMANYTE_SEEN,
    },
    0xD314: {
        0: constants.OMASTAR_SEEN,
        1: constants.JIGGLYPUFF_SEEN,
        2: constants.WIGGLYTUFF_SEEN,
        3: constants.EEVEE_SEEN,
        4: constants.FLAREON_SEEN,
        5: constants.JOLTEON_SEEN,
        6: constants.VAPOREON_SEEN,
        7: constants.MACHOP_SEEN,
    },
    0xD315: {
        0: constants.ZUBAT_SEEN,
        1: constants.EKANS_SEEN,
        2: constants.PARAS_SEEN,
        3: constants.POLIWHIRL_SEEN,
        4: constants.POLIWRATH_SEEN,
        5: constants.WEEDLE_SEEN,
        6: constants.KAKUNA_SEEN,
        7: constants.BEEDRILL_SEEN,
    },
    0xD316: {
        0: constants.DODRIO_SEEN,
        1: constants.PRIMEAPE_SEEN,
        2: constants.DUGTRIO_SEEN,
        3: constants.VENOMOTH_SEEN,
        4: constants.DEWGONG_SEEN,
        5: constants.CATERPIE_SEEN,
        6: constants.METAPOD_SEEN,
        7: constants.BUTTERFREE_SEEN,
    },
    0xD317: {
        0: constants.MACHAMP_SEEN,
        1: constants.GOLDUCK_SEEN,
        2: constants.HYPNO_SEEN,
        3: constants.GOLBAT_SEEN,
        4: constants.MEWTWO_SEEN,
        5: constants.SNORLAX_SEEN,
        6: constants.MAGIKARP_SEEN,
        7: constants.MUK_SEEN,
    },
    0xD318: {
        0: constants.KINGLER_SEEN,
        1: constants.CLOYSTER_SEEN,
        2: constants.ELECTRODE_SEEN,
        3: constants.CLEFABLE_SEEN,
        4: constants.WEEZING_SEEN,
        5: constants.PERSIAN_SEEN,
        6: constants.MAROWAK_SEEN,
        7: constants.HAUNTER_SEEN,
    },
    0xD319: {
        0: constants.ABRA_SEEN,
        1: constants.ALAKAZAM_SEEN,
        2: constants.PIDGEOTTO_SEEN,
        3: constants.PIDGEOT_SEEN,
        4: constants.STARMIE_SEEN,
        5: constants.BULBASAUR_SEEN,
        6: constants.VENUSAUR_SEEN,
        7: constants.TENTACRUEL_SEEN,
    },
    0xD31A: {
        0: constants.GOLDEEN_SEEN,
        1: constants.SEAKING_SEEN,
        2: constants.PONYTA_SEEN,
        3: constants.RAPIDASH_SEEN,
        4: constants.RATTATA_SEEN,
        5: constants.RATICATE_SEEN,
        6: constants.NIDORINO_SEEN,
        7: constants.NIDORINA_SEEN,
    },
    0xD31B: {
        0: constants.GEODUDE_SEEN,
        1: constants.PORYGON_SEEN,
        2: constants.AERODACTYL_SEEN,
        3: constants.MAGNEMITE_SEEN,
        4: constants.CHARMANDER_SEEN,
        5: constants.SQUIRTLE_SEEN,
        6: constants.CHARMELEON_SEEN,
        7: constants.WARTORTLE_SEEN,
    },
    0xD31C: {
        0: constants.CHARIZARD_SEEN,
        1: constants.ODDISH_SEEN,
        2: constants.GLOOM_SEEN,
        3: constants.VILEPLUME_SEEN,
        4: constants.BELLSPROUT_SEEN,
        5: constants.WEEPINBELL_SEEN,
        6: constants.VICTREEBEL_SEEN,
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
