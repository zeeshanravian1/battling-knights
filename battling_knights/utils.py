"""Utility functions for game.

Description:
- get_new_position: Function to get new position of knight.
- is_valid_position: Function to check if position is valid.
- execute_knight_move: Function to execute move of knight.
- execute_knight_fight: Function to execute fight of knight.
- handle_drowned_knight: Function to handle drowned knight.
- execute_move: Function to execute move of knight.

"""

import logging
from typing import TYPE_CHECKING

from .constants import DIRECTIONS, STATUS

if TYPE_CHECKING:
    from .models import Item, Knight

logger: logging.Logger = logging.getLogger(name=__name__)


def get_new_position(knight: Knight, direction: list[int]) -> list[int]:
    """Function to get new position of knight.

    :Description:
    - Gets new position of knight based on direction

    :Args:
    - `knight` (Knight): Knight to move
    - `direction` (list[int]): Direction to move

    :Returns:
    - `list[int]`: New position of knight

    """
    if knight.position is None:
        raise ValueError("Knight has no position")

    return [
        knight.position[0] + direction[0],
        knight.position[1] + direction[1],
    ]


def is_valid_position(position: list[int]) -> bool:
    """Function to check if position is valid.

    :Description:
    - Checks if position is valid on board

    :Args:
    - `position` (list[int]): Position to check

    :Returns:
    - `bool`: True if position is valid, False otherwise

    """
    return 0 <= position[0] < 8 and 0 <= position[1] < 8


def execute_knight_move(
    knight: Knight, items: dict[str, Item], new_position: list[int]
) -> None:
    """Function to execute move of knight.

    :Description:
    - Executes move of knight to new position

    :Args:
    - `knight` (Knight): Knight to move
    - `items` (dict[str, Item]): Dictionary of items
    - `new_position` (list[int]): New position of knight

    :Returns:
    - `None`

    """
    knight.position = new_position

    for item in items.values():
        if item.position == new_position:
            knight.item = item
            item.position = None
            break


def execute_knight_fight(knight: Knight, knights: dict[str, Knight]) -> None:
    """Function to execute fight of knight.

    :Description:
    - Executes fight of knight with other knights

    :Args:
    - `knight` (Knight): Knight to fight with
    - `knights` (dict[str, Knight]): Dictionary of knights

    :Returns:
    - `None`

    """
    for defender in knights.values():
        if (
            defender != knight
            and defender.position == knight.position
            and defender.status == STATUS.LIVE
        ):
            loser: Knight = knight.fight(defender)
            loser.status = STATUS.DEAD
            loser.item = None


def handle_drowned_knight(knight: Knight) -> None:
    """Function to handle drowned knight.

    :Description:
    - Handles drowned knight by setting their status to DROWNED

    :Args:
    - `knight` (Knight): Knight to handle

    :Returns:
    - `None`

    """
    knight.status = STATUS.DROWNED
    knight.position = None
    knight.attack = 0
    knight.defence = 0

    if knight.item:
        knight.item.position = knight.position
        knight.item = None

    logger.info("%s has drowned.", knight.name)


def execute_move(
    knights: dict[str, Knight], items: dict[str, Item], move: str
) -> None:
    """Function to execute move of knight.

    :Description:
    - Executes move of knight based on move

    :Args:
    - `knights` (dict[str, Knight]): Dictionary of knights
    - `items` (dict[str, Item]): Dictionary of items
    - `move` (str): Move to execute

    :Returns:
    - `None`

    :Raises:
    - `Exception`: If any error occurs during move execution

    """
    try:
        knight: Knight | None = knights.get(move[0])

        if knight and knight.status == STATUS.LIVE:
            direction: list[int] | None = DIRECTIONS.get(move[2])

            if direction:
                new_position: list[int] = get_new_position(knight, direction)

                if is_valid_position(new_position):
                    execute_knight_move(knight, items, new_position)
                    execute_knight_fight(knight, knights)
                    logger.debug("Move executed: %s", move)

                else:
                    handle_drowned_knight(knight)

            else:
                logger.warning(
                    "Invalid direction %s for move: %s", move[2], move
                )

        else:
            if knight is None:
                logger.info(
                    "%s cannot move because they are not found.", move[0]
                )
            else:
                logger.info(
                    "%s cannot move because they are %s.",
                    knight.name,
                    knight.status.value,
                )

    except Exception:
        logger.exception("Error executing move %s", move)
        raise
