# -*- coding: utf-8 -*-
"""
Utility functions for the game.

Description:
    - get_new_position: Function to get the new position of the knight
    - is_valid_position: Function to check if the position is valid
    - execute_knight_move: Function to execute the move of the knight
    - execute_knight_fight: Function to execute the fight of the knight
    - handle_drowned_knight: Function to handle the drowned knight
    - execute_move: Function to execute the move of the knight

"""

import logging

from .constants import DIRECTIONS, STATUS
from .models import Knight

logger: logging.Logger = logging.getLogger(__name__)


def get_new_position(knight, direction) -> list[int]:
    """
    Function to get the new position of the knight

    Description:
        - Gets the new position of the knight based on the direction

    Args:
        - `knight (Knight)`: Knight to move
        - `direction (list[int])`: Direction to move

    Returns:
        - `list[int]`: New position of the knight

    """

    return [
        knight.position[0] + direction[0],
        knight.position[1] + direction[1],
    ]


def is_valid_position(position) -> bool:
    """
    Function to check if the position is valid

    Description:
        - Checks if the position is valid on the board

    Args:
        - `position (list[int])`: Position to check

    Returns:
        - `bool`: True if the position is valid, False otherwise

    """

    return 0 <= position[0] < 8 and 0 <= position[1] < 8


def execute_knight_move(knight, items, new_position) -> None:
    """
    Function to execute the move of the knight

    Description:
        - Executes the move of the knight to the new position

    Args:
        - `knight (Knight)`: Knight to move
        - `items (dict[str, Item])`: Dictionary of items
        - `new_position (list[int])`: New position of the knight

    Returns:
        - `None`

    """

    knight.position = new_position
    for item in items.values():
        if item.position == new_position:
            knight.item = item
            item.position = None
            break


def execute_knight_fight(knight, knights) -> None:
    """
    Function to execute the fight of the knight

    Description:
        - Executes the fight of the knight with other knights

    Args:
        - `knight (Knight)`: Knight to fight
        - `knights (dict[str, Knight])`: Dictionary of knights

    Returns:
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


def handle_drowned_knight(knight) -> None:
    """
    Function to handle the drowned knight

    Description:
        - Handles the drowned knight by setting their status to DROWNED

    Args:
        - `knight (Knight)`: Knight to handle

    Returns:
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


def execute_move(knights, items, move) -> None:
    """
    Function to execute the move of the knight

    Description:
        - Executes the move of the knight based on the move

    Args:
        - `knights (dict[str, Knight])`: Dictionary of knights
        - `items (dict[str, Item])`: Dictionary of items
        - `move (str)`: Move to execute

    Returns:
        - `None`

    Raises:
        - `Exception`: If any error occurs during the move execution

    """

    try:
        knight: Knight = knights.get(move[0])

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
            logger.info(
                "%s cannot move because they are %s.",
                knight.name,
                knight.status.value,
            )

    except Exception as err:
        logger.error("Error executing move %s: %s", move, err, exc_info=True)
        raise
