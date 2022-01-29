from abc import ABC, abstractmethod, abstractstaticmethod
from typing import List, Tuple, Union

from black import Optional
from pydantic import BaseModel


class ChangeMeaning(BaseModel):

    #: Meaning of the change
    meaning: str

    #: Value associated with a meaning, for example the name of a location
    #: or the number of items in an inventory slot
    value: Union[str, int, bool]


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
