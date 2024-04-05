# -*- coding: utf-8 -*-
"""
Main file for the game

Description:
    - The main file for the game
    - The file reads the moves from the moves.txt file
    - Executes the moves and saves the final state to final_state.json

"""

import json
import logging
from typing import Any

from battling_knights.constants import STATUS
from battling_knights.models import (
    Item,
    ItemAttributes,
    Knight,
    KnightAttributes,
)
from battling_knights.utils import execute_move

# Setup logging
logging.basicConfig(
    filename="game.log",
    level=logging.DEBUG,
    format=(
        "%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s"
    ),
)

logger: logging.Logger = logging.getLogger(__name__)


def load_moves(filename) -> list[str]:
    """
    Load moves from the moves.txt file

    Description:
        - The function reads the moves from the moves.txt file
        - Returns a list of moves

    Args:
        - `filename (str)`: The name of the file to load moves from

    Returns:
        - `list[str]`: A list of moves

    Raises:
        - `FileNotFoundError`: If the file does not exist
        - `ValueError`: If GAME-START or GAME-END tag is missing
        - `Exception`: If any other error occurs

    """

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data: list[str] = file.read().split("\n")
            moves: list[str] = data[
                data.index("GAME-START") + 1 : data.index("GAME-END")
            ]
            logger.info("Moves loaded successfully.")

            return moves

    except FileNotFoundError as err:
        logger.error("File %s not found.", filename)
        raise err

    except ValueError as err:
        logger.error("GAME-START or GAME-END tag is missing.")
        raise err

    except Exception as err:
        logger.error("Failed to load moves from %s: %s", filename, err)
        raise err


def main() -> None:
    """
    Main function to execute the game

    Description:
        - The main function to execute the game
        - Loads the moves from the moves.txt file
        - Executes the moves
        - Saves the final state to final_state.json

    Args:
        - `None`

    Returns:
        - `None`

    Raises:
        - Exception: If any error occurs during game execution

    """

    knights: dict[str, Knight] = {
        "R": Knight(
            knight=KnightAttributes(
                code="R",
                name="Red",
                position=[0, 0],
            )
        ),
        "B": Knight(
            knight=KnightAttributes(
                code="B",
                name="Blue",
                position=[7, 0],
            )
        ),
        "G": Knight(
            knight=KnightAttributes(
                code="G",
                name="Green",
                position=[7, 7],
            )
        ),
        "Y": Knight(
            knight=KnightAttributes(
                code="Y",
                name="Yellow",
                position=[0, 7],
            )
        ),
    }

    items: dict[str, Item] = {
        "A": Item(
            item=ItemAttributes(
                code="A",
                name="Axe",
                attack=2,
                defence=0,
                priority=1,
                position=[2, 2],
            )
        ),
        "M": Item(
            item=ItemAttributes(
                code="M",
                name="MagicStaff",
                attack=1,
                defence=1,
                priority=2,
                position=[5, 2],
            )
        ),
        "D": Item(
            item=ItemAttributes(
                code="D",
                name="Dagger",
                attack=1,
                defence=0,
                priority=3,
                position=[2, 5],
            )
        ),
        "H": Item(
            item=ItemAttributes(
                code="H",
                name="Helmet",
                attack=0,
                defence=1,
                priority=4,
                position=[5, 5],
            )
        ),
    }

    try:
        moves: list[str] = load_moves("moves.txt")
        for move in moves:
            execute_move(knights, items, move)

        final_state: dict[
            str, list[list[int] | STATUS | str | int | float | None] | Any
        ] = {
            knight.name.lower(): knight.to_json()
            for knight in knights.values()
        }
        final_state.update(
            {item.name.lower(): item.to_json() for item in items.values()}
        )

        with open("final_state.json", "w", encoding="utf-8") as file:
            json.dump(final_state, file, indent=4)
        logger.info("Final state written to final_state.json")

    except Exception as err:
        logger.error("An error occurred during game execution: %s", err)


if __name__ == "__main__":
    main()
