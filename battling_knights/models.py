"""Models for game.

Description:
- Knight: Model for knight.
- Item: Model for item.

"""

from dataclasses import dataclass
from typing import Self

from .constants import STATUS


@dataclass
class ItemAttributes:
    """Model for item attributes.

    :Description:
    - ItemAttributes model to store attributes of item

    :Attributes:
    - `code` (str): Code of item.
    - `name` (str): Name of item.
    - `attack` (int): Attack power of item.
    - `defence` (int): Defence power of item.
    - `priority` (int): Priority of item.
    - `position` (list[int]): Position of item.

    """

    code: str
    name: str
    attack: int
    defence: int
    priority: int
    position: list[int]


class Item:
    """Model for item.

    :Description:
    - Item model to store details of item

    :Attributes:
    - `code` (str): Code of item.
    - `name` (str): Name of item.
    - `attack` (int): Attack power of item.
    - `defence` (int): Defence power of item.
    - `priority` (int): Priority of item.
    - `position` (list[int]): Position of item.

    :Methods:
    - `to_json`: Method to convert item to JSON format

    """

    def __init__(self, item: ItemAttributes) -> None:
        """Initialize item with given attributes.

        :Args:
        - `item` (ItemAttributes): Attributes of item

        :Returns:
        - `None`

        """
        self.code: str = item.code
        self.name: str = item.name
        self.attack: int = item.attack
        self.defence: int = item.defence
        self.priority: int = item.priority
        self.position: list[int] | None = item.position

    def to_json(self) -> list[list[int] | bool | None]:
        """Method to convert item to JSON format.

        :Description:
        - Converts item to JSON format

        :Args:
        - `None`

        :Returns:
        - `list[list[int] | bool | None]`: JSON representation of item

        """
        return [self.position, self.position is None]


@dataclass
class KnightAttributes:
    """Model for knight attributes.

    :Description:
    - KnightAttributes model to store attributes of knight

    :Attributes:
    - `code` (str): Code of knight.
    - `name` (str): Name of knight.
    - `position` (list[int] | None): Position of knight.
    - `status` (STATUS): Status of knight.
    - `item` (Item): Item equipped by knight.
    - `attack` (float): Attack power of knight.
    - `defence` (int): Defence power of knight.

    """

    code: str
    name: str
    position: list[int] | None
    item: Item | None = None
    status: STATUS = STATUS.LIVE
    attack: float = 1.0
    defence: int = 1


class Knight:
    """Model for knight.

    :Description:
    - Knight model to store details of knight

    :Attributes:
    - `code` (str): Code of knight.
    - `name` (str): Name of knight.
    - `position` (list[int] | None): Position of knight.
    - `status` (STATUS): Status of knight.
    - `item` (Item): Item equipped by knight.
    - `attack` (float): Attack power of knight.
    - `defence` (int): Defence power of knight.

    :Methods:
    - `fight`: Method to fight with another knight.
    - `to_json`: Method to convert knight to JSON format.

    """

    def __init__(
        self,
        knight: KnightAttributes,
    ) -> None:
        """Constructor to initialize knight with given attributes.

        :Description:
        - Initializes knight with provided KnightAttributes.

        :Args:
        - `knight (KnightAttributes)`: Attributes of knight to initialize

        :Returns:
        - `None`

        """
        self.code: str = knight.code
        self.name: str = knight.name
        self.position: list[int] | None = knight.position
        self.status: STATUS = knight.status
        self.item: Item | None = knight.item
        self.attack: float = knight.attack
        self.defence: int = knight.defence

    def fight(self, defender: Self) -> Self:
        """Method to fight with another knight.

        :Description:
        - Method to fight with another knight.
        - Knight with higher attack power wins.
        - Loser's attack and defence power is set to 0.

        :Args:
        - `defender (Knight)`: Knight to fight with

        :Returns:
        - `Knight`: Loser of fight

        """
        total_attack: float = (
            self.attack + (self.item.attack if self.item else 0) + 0.5
        )
        total_defence: int = defender.defence + (
            defender.item.defence if defender.item else 0
        )
        loser: Self = defender if total_attack > total_defence else self
        loser.attack = 0
        loser.defence = 0

        return loser

    def to_json(self) -> list[list[int] | STATUS | str | int | float | None]:
        """Method to convert knight to JSON format.

        :Description:
        - Converts knight to JSON format

        :Args:
        - `None`

        :Returns:
        - `list[list[int] | STATUS | str | None | int]`: JSON
        representation of knight

        """
        return [
            self.position,
            self.status.value,
            self.item.name if self.item else None,
            self.attack,
            self.defence,
        ]
