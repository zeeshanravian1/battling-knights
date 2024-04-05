# -*- coding: utf-8 -*-
"""
Constants used in the project

Description:
    - STATUS: Enum for the status of the player
    - DIRECTIONS: Dictionary for the directions the player can move

"""

from enum import Enum


class STATUS(Enum):
    """
    Enum for the status of the player

    Attributes:
        - LIVE: Player is alive
        - DEAD: Player is dead
        - DROWNED: Player is drowned

    """

    LIVE = "LIVE"
    DEAD = "DEAD"
    DROWNED = "DROWNED"


DIRECTIONS: dict[str, list[int]] = {
    "N": [-1, 0],
    "S": [1, 0],
    "E": [0, 1],
    "W": [0, -1],
}
