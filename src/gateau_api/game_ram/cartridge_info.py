from abc import ABC, abstractmethod, abstractstaticmethod
from typing import List, Tuple

from black import Optional
from pydantic import BaseModel


class ChangeMeaning(BaseModel):

    #: Meaning of the change
    meaning: str

    #: If True, the new value is positive. If False, the new value is negative.
    positive: bool


class CartridgeInfo(ABC):
    """
    Info for a specific cartridge
    """

    @abstractstaticmethod
    def byte_for_meaning(meaning: str) -> int:
        """
        Get the address corresponding to a specific meaning for a given
        cartridge.

        Raises
        ------
        ValueError
            If the meaning doesn't apply to this cartridge
        """

    @abstractstaticmethod
    def meaning_for_byte_change(
        address: int,
        old_value: int,
        new_value: int,
    ) -> List[ChangeMeaning]:
        """
        Meanings corresponding to a change in byte value from one to another.

        There may be multiple meanings of a change, for example if the byte
        corresponds to several single-bit values
        """
