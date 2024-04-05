# -*- coding: utf-8 -*-
"""
Models for the game

Description:
    - Knight: Model for the knight
    - Item: Model for the item

"""

from dataclasses import dataclass

from typing_extensions import Self

from .constants import STATUS


@dataclass
class ItemAttributes:
    """
    Model for the item attributes

    Description:
        - ItemAttributes model to store the attributes of the item

    Attributes:
        - `code (str)`: Code of the item
        - `name (str)`: Name of the item
        - `attack (int)`: Attack power of the item
        - `defence (int)`: Defence power of the item
        - `priority (int)`: Priority of the item
        - `position (list[int])`: Position of the item

    """

    code: str
    name: str
    attack: int
    defence: int
    priority: int
    position: list[int]


class Item:
    """
    Model for the item

    Description:
        - Item model to store the details of the item

    Attributes:
        - `code (str)`: Code of the item
        - `name (str)`: Name of the item
        - `attack (int)`: Attack power of the item
        - `defence (int)`: Defence power of the item
        - `priority (int)`: Priority of the item
        - `position (list[int])`: Position of the item

    Methods:
        - `to_json`: Method to convert the item to JSON format

    """

    def __init__(self, item: ItemAttributes) -> None:
        self.code: str = item.code
        self.name: str = item.name
        self.attack: int = item.attack
        self.defence: int = item.defence
        self.priority: int = item.priority
        self.position: list[int] = item.position

    def to_json(self) -> list[list[int] | bool]:
        """
        Method to convert the item to JSON format

        Description:
            - Converts the item to JSON format

        Args:
            - `None`

        Returns:
            - `list[list[int] | bool]`: JSON representation of the item

        """

        return [self.position, self.position is None]


@dataclass
class KnightAttributes:
    """
    Model for the knight attributes

    Description:
        - KnightAttributes model to store the attributes of the knight

    Attributes:
        - `code (str)`: Code of the knight
        - `name (str)`: Name of the knight
        - `position (list[int])`: Position of the knight
        - `status (STATUS)`: Status of the knight
        - `item` (Item)`: Item equipped by the knight
        - `attack (float)`: Attack power of the knight
        - `defence (int)`: Defence power of the knight

    """

    code: str
    name: str
    position: list[int]
    item: Item | None = None
    status: STATUS = STATUS.LIVE
    attack: float = 1.0
    defence: int = 1


class Knight:
    """
    Model for the knight

    Description:
        - Knight model to store the details of the knight

    Attributes:
        - `code (str)`: Code of the knight
        - `name (str)`: Name of the knight
        - `position (list[int])`: Position of the knight
        - `status (STATUS)`: Status of the knight
        - `item` (Item)`: Item equipped by the knight
        - `attack (float)`: Attack power of the knight
        - `defence (int)`: Defence power of the knight

    Methods:
        - `fight`: Method to fight with another knight
        - `to_json`: Method to convert the knight to JSON format

    """

    def __init__(
        self,
        knight: KnightAttributes,
    ) -> None:
        self.code: str = knight.code
        self.name: str = knight.name
        self.position: list[int] = knight.position
        self.status: STATUS = knight.status
        self.item: Item | None = knight.item
        self.attack: float = knight.attack
        self.defence: int = knight.defence

    def fight(self, defender) -> Self:
        """
        Method to fight with another knight

        Description:
            - Method to fight with another knight
            - The knight with higher attack power wins
            - The loser's attack and defence power is set to 0

        Args:
            - `defender (Knight)`: Knight to fight with

        Returns:
            - `Knight`: The loser of the fight

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
        """
        Method to convert the knight to JSON format

        Description:
            - Converts the knight to JSON format

        Args:
            - `None`

        Returns:
            - `list[list[int] | STATUS | str | None | int]`: JSON
            representation of the knight

        """

        return [
            self.position,
            self.status.value,
            self.item.name if self.item else None,
            self.attack,
            self.defence,
        ]
