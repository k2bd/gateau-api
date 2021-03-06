from typing import List, Optional

from gateau_api.game_ram.cartridge_info import CartridgeInfo, ChangeMeaning
from gateau_api.game_ram.pokemon import constants

#: Bit to meaning
BIT_TO_MEANING = {
    0xDE99: {
        7: constants.CHIKORITA_OWNED,
        6: constants.BAYLEEF_OWNED,
        5: constants.MEGANIUM_OWNED,
        4: constants.CYNDAQUIL_OWNED,
        3: constants.QUILAVA_OWNED,
        2: constants.TYPHLOSION_OWNED,
        1: constants.TOTODILE_OWNED,
        0: constants.CROCONAW_OWNED,
    },
    0xDE9A: {
        7: constants.FERALIGATR_OWNED,
        6: constants.PIDGEY_OWNED,
        5: constants.PIDGEOTTO_OWNED,
        4: constants.PIDGEOT_OWNED,
        3: constants.SPEAROW_OWNED,
        2: constants.FEAROW_OWNED,
        1: constants.HOOTHOOT_OWNED,
        0: constants.NOCTOWL_OWNED,
    },
    0xDE9B: {
        7: constants.RATTATA_OWNED,
        6: constants.RATICATE_OWNED,
        5: constants.SENTRET_OWNED,
        4: constants.FURRET_OWNED,
        3: constants.PICHU_OWNED,
        2: constants.PIKACHU_OWNED,
        1: constants.RAICHU_OWNED,
        0: constants.CATERPIE_OWNED,
    },
    0xDE9C: {
        7: constants.METAPOD_OWNED,
        6: constants.BUTTERFREE_OWNED,
        5: constants.WEEDLE_OWNED,
        4: constants.KAKUNA_OWNED,
        3: constants.BEEDRILL_OWNED,
        2: constants.LEDYBA_OWNED,
        1: constants.LEDIAN_OWNED,
        0: constants.SPINARAK_OWNED,
    },
    0xDE9D: {
        7: constants.ARIADOS_OWNED,
        6: constants.GEODUDE_OWNED,
        5: constants.GRAVELER_OWNED,
        4: constants.GOLEM_OWNED,
        3: constants.ZUBAT_OWNED,
        2: constants.GOLBAT_OWNED,
        1: constants.CROBAT_OWNED,
        0: constants.CLEFFA_OWNED,
    },
    0xDE9E: {
        7: constants.CLEFAIRY_OWNED,
        6: constants.CLEFABLE_OWNED,
        5: constants.IGGLYBUFF_OWNED,
        4: constants.JIGGLYPUFF_OWNED,
        3: constants.WIGGLYTUFF_OWNED,
        2: constants.TOGEPI_OWNED,
        1: constants.TOGETIC_OWNED,
        0: constants.SANDSHREW_OWNED,
    },
    0xDE9F: {
        7: constants.SANDSLASH_OWNED,
        6: constants.EKANS_OWNED,
        5: constants.ARBOK_OWNED,
        4: constants.DUNSPARCE_OWNED,
        3: constants.MAREEP_OWNED,
        2: constants.FLAAFFY_OWNED,
        1: constants.AMPHAROS_OWNED,
        0: constants.WOOPER_OWNED,
    },
    0xDEA0: {
        7: constants.QUAGSIRE_OWNED,
        6: constants.GASTLY_OWNED,
        5: constants.HAUNTER_OWNED,
        4: constants.GENGAR_OWNED,
        3: constants.UNOWN_OWNED,
        2: constants.ONIX_OWNED,
        1: constants.STEELIX_OWNED,
        0: constants.BELLSPROUT_OWNED,
    },
    0xDEA1: {
        7: constants.WEEPINBELL_OWNED,
        6: constants.VICTREEBEL_OWNED,
        5: constants.HOPPIP_OWNED,
        4: constants.SKIPLOOM_OWNED,
        3: constants.JUMPLUFF_OWNED,
        2: constants.PARAS_OWNED,
        1: constants.PARASECT_OWNED,
        0: constants.POLIWAG_OWNED,
    },
    0xDEA2: {
        7: constants.POLIWHIRL_OWNED,
        6: constants.POLIWRATH_OWNED,
        5: constants.POLITOED_OWNED,
        4: constants.MAGIKARP_OWNED,
        3: constants.GYARADOS_OWNED,
        2: constants.GOLDEEN_OWNED,
        1: constants.SEAKING_OWNED,
        0: constants.SLOWPOKE_OWNED,
    },
    0xDEA3: {
        7: constants.SLOWBRO_OWNED,
        6: constants.SLOWKING_OWNED,
        5: constants.ODDISH_OWNED,
        4: constants.GLOOM_OWNED,
        3: constants.VILEPLUME_OWNED,
        2: constants.BELLOSSOM_OWNED,
        1: constants.DROWZEE_OWNED,
        0: constants.HYPNO_OWNED,
    },
    0xDEA4: {
        7: constants.ABRA_OWNED,
        6: constants.KADABRA_OWNED,
        5: constants.ALAKAZAM_OWNED,
        4: constants.DITTO_OWNED,
        3: constants.PINECO_OWNED,
        2: constants.FORRETRESS_OWNED,
        1: constants.NIDORAN_F_OWNED,
        0: constants.NIDORINA_OWNED,
    },
    0xDEA5: {
        7: constants.NIDOQUEEN_OWNED,
        6: constants.NIDORAN_M_OWNED,
        5: constants.NIDORINO_OWNED,
        4: constants.NIDOKING_OWNED,
        3: constants.YANMA_OWNED,
        2: constants.SUNKERN_OWNED,
        1: constants.SUNFLORA_OWNED,
        0: constants.EXEGGCUTE_OWNED,
    },
    0xDEA6: {
        7: constants.EXEGGUTOR_OWNED,
        6: constants.SUDOWOODO_OWNED,
        5: constants.WOBBUFFET_OWNED,
        4: constants.VENONAT_OWNED,
        3: constants.VENOMOTH_OWNED,
        2: constants.SCYTHER_OWNED,
        1: constants.SCIZOR_OWNED,
        0: constants.PINSIR_OWNED,
    },
    0xDEA7: {
        7: constants.HERACROSS_OWNED,
        6: constants.KOFFING_OWNED,
        5: constants.WEEZING_OWNED,
        4: constants.GRIMER_OWNED,
        3: constants.MUK_OWNED,
        2: constants.MAGNEMITE_OWNED,
        1: constants.MAGNETON_OWNED,
        0: constants.VOLTORB_OWNED,
    },
    0xDEA8: {
        7: constants.ELECTRODE_OWNED,
        6: constants.AIPOM_OWNED,
        5: constants.SNUBBULL_OWNED,
        4: constants.GRANBULL_OWNED,
        3: constants.VULPIX_OWNED,
        2: constants.NINETALES_OWNED,
        1: constants.GROWLITHE_OWNED,
        0: constants.ARCANINE_OWNED,
    },
    0xDEA9: {
        7: constants.STANTLER_OWNED,
        6: constants.MARILL_OWNED,
        5: constants.AZUMARILL_OWNED,
        4: constants.DIGLETT_OWNED,
        3: constants.DUGTRIO_OWNED,
        2: constants.MANKEY_OWNED,
        1: constants.PRIMEAPE_OWNED,
        0: constants.MEOWTH_OWNED,
    },
    0xDEAA: {
        7: constants.PERSIAN_OWNED,
        6: constants.PSYDUCK_OWNED,
        5: constants.GOLDUCK_OWNED,
        4: constants.MACHOP_OWNED,
        3: constants.MACHOKE_OWNED,
        2: constants.MACHAMP_OWNED,
        1: constants.TYROGUE_OWNED,
        0: constants.HITMONLEE_OWNED,
    },
    0xDEAB: {
        7: constants.HITMONCHAN_OWNED,
        6: constants.HITMONTOP_OWNED,
        5: constants.GIRAFARIG_OWNED,
        4: constants.TAUROS_OWNED,
        3: constants.MILTANK_OWNED,
        2: constants.MAGBY_OWNED,
        1: constants.MAGMAR_OWNED,
        0: constants.SMOOCHUM_OWNED,
    },
    0xDEAC: {
        7: constants.JYNX_OWNED,
        6: constants.ELEKID_OWNED,
        5: constants.ELECTABUZZ_OWNED,
        4: constants.MRMIME_OWNED,
        3: constants.SMEARGLE_OWNED,
        2: constants.FARFETCHD_OWNED,
        1: constants.NATU_OWNED,
        0: constants.XATU_OWNED,
    },
    0xDEAD: {
        7: constants.QWILFISH_OWNED,
        6: constants.TENTACOOL_OWNED,
        5: constants.TENTACRUEL_OWNED,
        4: constants.KRABBY_OWNED,
        3: constants.KINGLER_OWNED,
        2: constants.SHUCKLE_OWNED,
        1: constants.STARYU_OWNED,
        0: constants.STARMIE_OWNED,
    },
    0xDEAE: {
        7: constants.SHELLDER_OWNED,
        6: constants.CLOYSTER_OWNED,
        5: constants.CORSOLA_OWNED,
        4: constants.REMORAID_OWNED,
        3: constants.OCTILLERY_OWNED,
        2: constants.CHINCHOU_OWNED,
        1: constants.LANTURN_OWNED,
        0: constants.SEEL_OWNED,
    },
    0xDEAF: {
        7: constants.DEWGONG_OWNED,
        6: constants.LICKITUNG_OWNED,
        5: constants.TANGELA_OWNED,
        4: constants.EEVEE_OWNED,
        3: constants.VAPOREON_OWNED,
        2: constants.JOLTEON_OWNED,
        1: constants.FLAREON_OWNED,
        0: constants.ESPEON_OWNED,
    },
    0xDEB0: {
        7: constants.UMBREON_OWNED,
        6: constants.HORSEA_OWNED,
        5: constants.SEADRA_OWNED,
        4: constants.KINGDRA_OWNED,
        3: constants.GLIGAR_OWNED,
        2: constants.DELIBIRD_OWNED,
        1: constants.SWINUB_OWNED,
        0: constants.PILOSWINE_OWNED,
    },
    0xDEB1: {
        7: constants.TEDDIURSA_OWNED,
        6: constants.URSARING_OWNED,
        5: constants.PHANPY_OWNED,
        4: constants.DONPHAN_OWNED,
        3: constants.MANTINE_OWNED,
        2: constants.SKARMORY_OWNED,
        1: constants.DODUO_OWNED,
        0: constants.DODRIO_OWNED,
    },
    0xDEB2: {
        7: constants.PONYTA_OWNED,
        6: constants.RAPIDASH_OWNED,
        5: constants.CUBONE_OWNED,
        4: constants.MAROWAK_OWNED,
        3: constants.KANGASKHAN_OWNED,
        2: constants.RHYHORN_OWNED,
        1: constants.RHYDON_OWNED,
        0: constants.MURKROW_OWNED,
    },
    0xDEB3: {
        7: constants.HOUNDOUR_OWNED,
        6: constants.HOUNDOOM_OWNED,
        5: constants.SLUGMA_OWNED,
        4: constants.MAGCARGO_OWNED,
        3: constants.SNEASEL_OWNED,
        2: constants.MISDREAVUS_OWNED,
        1: constants.PORYGON_OWNED,
        0: constants.PORYGON2_OWNED,
    },
    0xDEB4: {
        7: constants.CHANSEY_OWNED,
        6: constants.BLISSEY_OWNED,
        5: constants.LAPRAS_OWNED,
        4: constants.OMANYTE_OWNED,
        3: constants.OMASTAR_OWNED,
        2: constants.KABUTO_OWNED,
        1: constants.KABUTOPS_OWNED,
        0: constants.AERODACTYL_OWNED,
    },
    0xDEB5: {
        7: constants.SNORLAX_OWNED,
        6: constants.BULBASAUR_OWNED,
        5: constants.IVYSAUR_OWNED,
        4: constants.VENUSAUR_OWNED,
        3: constants.CHARMANDER_OWNED,
        2: constants.CHARMELEON_OWNED,
        1: constants.CHARIZARD_OWNED,
        0: constants.SQUIRTLE_OWNED,
    },
    0xDEB6: {
        7: constants.WARTORTLE_OWNED,
        6: constants.BLASTOISE_OWNED,
        5: constants.ARTICUNO_OWNED,
        4: constants.ZAPDOS_OWNED,
        3: constants.MOLTRES_OWNED,
        2: constants.RAIKOU_OWNED,
        1: constants.ENTEI_OWNED,
        0: constants.SUICUNE_OWNED,
    },
    0xDEB7: {
        7: constants.DRATINI_OWNED,
        6: constants.DRAGONAIR_OWNED,
        5: constants.DRAGONITE_OWNED,
        4: constants.LARVITAR_OWNED,
        3: constants.PUPITAR_OWNED,
        2: constants.TYRANITAR_OWNED,
        1: constants.LUGIA_OWNED,
        0: constants.HO_OH_OWNED,
    },
    0xDEB8: {
        7: constants.MEWTWO_OWNED,
        6: constants.MEW_OWNED,
        5: constants.CELEBI_OWNED,
    },
    0xDEB9: {
        7: constants.CHIKORITA_SEEN,
        6: constants.BAYLEEF_SEEN,
        5: constants.MEGANIUM_SEEN,
        4: constants.CYNDAQUIL_SEEN,
        3: constants.QUILAVA_SEEN,
        2: constants.TYPHLOSION_SEEN,
        1: constants.TOTODILE_SEEN,
        0: constants.CROCONAW_SEEN,
    },
    0xDEBA: {
        7: constants.FERALIGATR_SEEN,
        6: constants.PIDGEY_SEEN,
        5: constants.PIDGEOTTO_SEEN,
        4: constants.PIDGEOT_SEEN,
        3: constants.SPEAROW_SEEN,
        2: constants.FEAROW_SEEN,
        1: constants.HOOTHOOT_SEEN,
        0: constants.NOCTOWL_SEEN,
    },
    0xDEBB: {
        7: constants.RATTATA_SEEN,
        6: constants.RATICATE_SEEN,
        5: constants.SENTRET_SEEN,
        4: constants.FURRET_SEEN,
        3: constants.PICHU_SEEN,
        2: constants.PIKACHU_SEEN,
        1: constants.RAICHU_SEEN,
        0: constants.CATERPIE_SEEN,
    },
    0xDEBC: {
        7: constants.METAPOD_SEEN,
        6: constants.BUTTERFREE_SEEN,
        5: constants.WEEDLE_SEEN,
        4: constants.KAKUNA_SEEN,
        3: constants.BEEDRILL_SEEN,
        2: constants.LEDYBA_SEEN,
        1: constants.LEDIAN_SEEN,
        0: constants.SPINARAK_SEEN,
    },
    0xDEBD: {
        7: constants.ARIADOS_SEEN,
        6: constants.GEODUDE_SEEN,
        5: constants.GRAVELER_SEEN,
        4: constants.GOLEM_SEEN,
        3: constants.ZUBAT_SEEN,
        2: constants.GOLBAT_SEEN,
        1: constants.CROBAT_SEEN,
        0: constants.CLEFFA_SEEN,
    },
    0xDEBE: {
        7: constants.CLEFAIRY_SEEN,
        6: constants.CLEFABLE_SEEN,
        5: constants.IGGLYBUFF_SEEN,
        4: constants.JIGGLYPUFF_SEEN,
        3: constants.WIGGLYTUFF_SEEN,
        2: constants.TOGEPI_SEEN,
        1: constants.TOGETIC_SEEN,
        0: constants.SANDSHREW_SEEN,
    },
    0xDEBF: {
        7: constants.SANDSLASH_SEEN,
        6: constants.EKANS_SEEN,
        5: constants.ARBOK_SEEN,
        4: constants.DUNSPARCE_SEEN,
        3: constants.MAREEP_SEEN,
        2: constants.FLAAFFY_SEEN,
        1: constants.AMPHAROS_SEEN,
        0: constants.WOOPER_SEEN,
    },
    0xDEC0: {
        7: constants.QUAGSIRE_SEEN,
        6: constants.GASTLY_SEEN,
        5: constants.HAUNTER_SEEN,
        4: constants.GENGAR_SEEN,
        3: constants.UNOWN_SEEN,
        2: constants.ONIX_SEEN,
        1: constants.STEELIX_SEEN,
        0: constants.BELLSPROUT_SEEN,
    },
    0xDEC1: {
        7: constants.WEEPINBELL_SEEN,
        6: constants.VICTREEBEL_SEEN,
        5: constants.HOPPIP_SEEN,
        4: constants.SKIPLOOM_SEEN,
        3: constants.JUMPLUFF_SEEN,
        2: constants.PARAS_SEEN,
        1: constants.PARASECT_SEEN,
        0: constants.POLIWAG_SEEN,
    },
    0xDEC2: {
        7: constants.POLIWHIRL_SEEN,
        6: constants.POLIWRATH_SEEN,
        5: constants.POLITOED_SEEN,
        4: constants.MAGIKARP_SEEN,
        3: constants.GYARADOS_SEEN,
        2: constants.GOLDEEN_SEEN,
        1: constants.SEAKING_SEEN,
        0: constants.SLOWPOKE_SEEN,
    },
    0xDEC3: {
        7: constants.SLOWBRO_SEEN,
        6: constants.SLOWKING_SEEN,
        5: constants.ODDISH_SEEN,
        4: constants.GLOOM_SEEN,
        3: constants.VILEPLUME_SEEN,
        2: constants.BELLOSSOM_SEEN,
        1: constants.DROWZEE_SEEN,
        0: constants.HYPNO_SEEN,
    },
    0xDEC4: {
        7: constants.ABRA_SEEN,
        6: constants.KADABRA_SEEN,
        5: constants.ALAKAZAM_SEEN,
        4: constants.DITTO_SEEN,
        3: constants.PINECO_SEEN,
        2: constants.FORRETRESS_SEEN,
        1: constants.NIDORAN_F_SEEN,
        0: constants.NIDORINA_SEEN,
    },
    0xDEC5: {
        7: constants.NIDOQUEEN_SEEN,
        6: constants.NIDORAN_M_SEEN,
        5: constants.NIDORINO_SEEN,
        4: constants.NIDOKING_SEEN,
        3: constants.YANMA_SEEN,
        2: constants.SUNKERN_SEEN,
        1: constants.SUNFLORA_SEEN,
        0: constants.EXEGGCUTE_SEEN,
    },
    0xDEC6: {
        7: constants.EXEGGUTOR_SEEN,
        6: constants.SUDOWOODO_SEEN,
        5: constants.WOBBUFFET_SEEN,
        4: constants.VENONAT_SEEN,
        3: constants.VENOMOTH_SEEN,
        2: constants.SCYTHER_SEEN,
        1: constants.SCIZOR_SEEN,
        0: constants.PINSIR_SEEN,
    },
    0xDEC7: {
        7: constants.HERACROSS_SEEN,
        6: constants.KOFFING_SEEN,
        5: constants.WEEZING_SEEN,
        4: constants.GRIMER_SEEN,
        3: constants.MUK_SEEN,
        2: constants.MAGNEMITE_SEEN,
        1: constants.MAGNETON_SEEN,
        0: constants.VOLTORB_SEEN,
    },
    0xDEC8: {
        7: constants.ELECTRODE_SEEN,
        6: constants.AIPOM_SEEN,
        5: constants.SNUBBULL_SEEN,
        4: constants.GRANBULL_SEEN,
        3: constants.VULPIX_SEEN,
        2: constants.NINETALES_SEEN,
        1: constants.GROWLITHE_SEEN,
        0: constants.ARCANINE_SEEN,
    },
    0xDEC9: {
        7: constants.STANTLER_SEEN,
        6: constants.MARILL_SEEN,
        5: constants.AZUMARILL_SEEN,
        4: constants.DIGLETT_SEEN,
        3: constants.DUGTRIO_SEEN,
        2: constants.MANKEY_SEEN,
        1: constants.PRIMEAPE_SEEN,
        0: constants.MEOWTH_SEEN,
    },
    0xDECA: {
        7: constants.PERSIAN_SEEN,
        6: constants.PSYDUCK_SEEN,
        5: constants.GOLDUCK_SEEN,
        4: constants.MACHOP_SEEN,
        3: constants.MACHOKE_SEEN,
        2: constants.MACHAMP_SEEN,
        1: constants.TYROGUE_SEEN,
        0: constants.HITMONLEE_SEEN,
    },
    0xDECB: {
        7: constants.HITMONCHAN_SEEN,
        6: constants.HITMONTOP_SEEN,
        5: constants.GIRAFARIG_SEEN,
        4: constants.TAUROS_SEEN,
        3: constants.MILTANK_SEEN,
        2: constants.MAGBY_SEEN,
        1: constants.MAGMAR_SEEN,
        0: constants.SMOOCHUM_SEEN,
    },
    0xDECC: {
        7: constants.JYNX_SEEN,
        6: constants.ELEKID_SEEN,
        5: constants.ELECTABUZZ_SEEN,
        4: constants.MRMIME_SEEN,
        3: constants.SMEARGLE_SEEN,
        2: constants.FARFETCHD_SEEN,
        1: constants.NATU_SEEN,
        0: constants.XATU_SEEN,
    },
    0xDECD: {
        7: constants.QWILFISH_SEEN,
        6: constants.TENTACOOL_SEEN,
        5: constants.TENTACRUEL_SEEN,
        4: constants.KRABBY_SEEN,
        3: constants.KINGLER_SEEN,
        2: constants.SHUCKLE_SEEN,
        1: constants.STARYU_SEEN,
        0: constants.STARMIE_SEEN,
    },
    0xDECE: {
        7: constants.SHELLDER_SEEN,
        6: constants.CLOYSTER_SEEN,
        5: constants.CORSOLA_SEEN,
        4: constants.REMORAID_SEEN,
        3: constants.OCTILLERY_SEEN,
        2: constants.CHINCHOU_SEEN,
        1: constants.LANTURN_SEEN,
        0: constants.SEEL_SEEN,
    },
    0xDECF: {
        7: constants.DEWGONG_SEEN,
        6: constants.LICKITUNG_SEEN,
        5: constants.TANGELA_SEEN,
        4: constants.EEVEE_SEEN,
        3: constants.VAPOREON_SEEN,
        2: constants.JOLTEON_SEEN,
        1: constants.FLAREON_SEEN,
        0: constants.ESPEON_SEEN,
    },
    0xDED0: {
        7: constants.UMBREON_SEEN,
        6: constants.HORSEA_SEEN,
        5: constants.SEADRA_SEEN,
        4: constants.KINGDRA_SEEN,
        3: constants.GLIGAR_SEEN,
        2: constants.DELIBIRD_SEEN,
        1: constants.SWINUB_SEEN,
        0: constants.PILOSWINE_SEEN,
    },
    0xDED1: {
        7: constants.TEDDIURSA_SEEN,
        6: constants.URSARING_SEEN,
        5: constants.PHANPY_SEEN,
        4: constants.DONPHAN_SEEN,
        3: constants.MANTINE_SEEN,
        2: constants.SKARMORY_SEEN,
        1: constants.DODUO_SEEN,
        0: constants.DODRIO_SEEN,
    },
    0xDED2: {
        7: constants.PONYTA_SEEN,
        6: constants.RAPIDASH_SEEN,
        5: constants.CUBONE_SEEN,
        4: constants.MAROWAK_SEEN,
        3: constants.KANGASKHAN_SEEN,
        2: constants.RHYHORN_SEEN,
        1: constants.RHYDON_SEEN,
        0: constants.MURKROW_SEEN,
    },
    0xDED3: {
        7: constants.HOUNDOUR_SEEN,
        6: constants.HOUNDOOM_SEEN,
        5: constants.SLUGMA_SEEN,
        4: constants.MAGCARGO_SEEN,
        3: constants.SNEASEL_SEEN,
        2: constants.MISDREAVUS_SEEN,
        1: constants.PORYGON_SEEN,
        0: constants.PORYGON2_SEEN,
    },
    0xDED4: {
        7: constants.CHANSEY_SEEN,
        6: constants.BLISSEY_SEEN,
        5: constants.LAPRAS_SEEN,
        4: constants.OMANYTE_SEEN,
        3: constants.OMASTAR_SEEN,
        2: constants.KABUTO_SEEN,
        1: constants.KABUTOPS_SEEN,
        0: constants.AERODACTYL_SEEN,
    },
    0xDED5: {
        7: constants.SNORLAX_SEEN,
        6: constants.BULBASAUR_SEEN,
        5: constants.IVYSAUR_SEEN,
        4: constants.VENUSAUR_SEEN,
        3: constants.CHARMANDER_SEEN,
        2: constants.CHARMELEON_SEEN,
        1: constants.CHARIZARD_SEEN,
        0: constants.SQUIRTLE_SEEN,
    },
    0xDED6: {
        7: constants.WARTORTLE_SEEN,
        6: constants.BLASTOISE_SEEN,
        5: constants.ARTICUNO_SEEN,
        4: constants.ZAPDOS_SEEN,
        3: constants.MOLTRES_SEEN,
        2: constants.RAIKOU_SEEN,
        1: constants.ENTEI_SEEN,
        0: constants.SUICUNE_SEEN,
    },
    0xDED7: {
        7: constants.DRATINI_SEEN,
        6: constants.DRAGONAIR_SEEN,
        5: constants.DRAGONITE_SEEN,
        4: constants.LARVITAR_SEEN,
        3: constants.PUPITAR_SEEN,
        2: constants.TYRANITAR_SEEN,
        1: constants.LUGIA_SEEN,
        0: constants.HO_OH_SEEN,
    },
    0xDED8: {
        7: constants.MEWTWO_SEEN,
        6: constants.MEW_SEEN,
        5: constants.CELEBI_SEEN,
    },
}

#: Bit-value meaning to byte address and bit
MEANING_TO_BIT = {}
for address, values in BIT_TO_MEANING.items():
    for bit, meaning in values.items():
        MEANING_TO_BIT[meaning] = (address, bit)


class PokemonCrystalInfo(CartridgeInfo):
    @staticmethod
    def byte_for_meaning(meaning: str) -> Optional[int]:
        """
        Get the address corresponding to a specific meaning for a given
        cartridge.

        If the meaning corresponds to a single bit within a byte, return the
        address of that byte

        Returns None if there is no corresponding byte.
        """

        if meaning in MEANING_TO_BIT:
            address, bit = MEANING_TO_BIT[meaning]
            return address

        return None

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

        if address in BIT_TO_MEANING:
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
                    meaning = BIT_TO_MEANING[address][change]
                except KeyError:
                    continue
                positive = new_bits[change] == 1
                results.append(ChangeMeaning(meaning=meaning, value=positive))

            return results

        return []
