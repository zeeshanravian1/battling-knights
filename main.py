"""Main file for game.

Description:
- Main file for game.
- File reads moves from moves.txt file.
- Executes moves and saves final state to final_state.json.

"""

import json
import logging
from typing import TYPE_CHECKING, Any

from battling_knights.models import (
    Item,
    ItemAttributes,
    Knight,
    KnightAttributes,
)
from battling_knights.utils import execute_move

if TYPE_CHECKING:
    from battling_knights.constants import STATUS

# Setup logging
logging.basicConfig(
    filename="game.log",
    level=logging.DEBUG,
    format=(
        "%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s"
    ),
)

logger: logging.Logger = logging.getLogger(name=__name__)


def load_moves(filename: str) -> list[str]:
    """Load moves from moves.txt file.

    :Description:
    - Function reads moves from moves.txt file.
    - Returns a list of moves.

    :Args:
    - `filename (str)`: Name of file to load moves from.

    :Returns:
    - `list[str]`: A list of moves.

    :Raises:
    - `FileNotFoundError`: If file does not exist.
    - `ValueError`: If GAME-START or GAME-END tag is missing.
    - `Exception`: If any other error occurs.

    """
    try:
        with open(file=filename, encoding="utf-8") as file:
            data: list[str] = file.read().split(sep="\n")
            moves: list[str] = data[
                data.index("GAME-START") + 1 : data.index("GAME-END")
            ]
            logger.info(msg="Moves loaded successfully.")

            return moves

    except FileNotFoundError:
        logger.error("File %s not found.", filename)
        raise

    except ValueError:
        logger.error(msg="GAME-START or GAME-END tag is missing.")
        raise

    except Exception as err:
        logger.error("Failed to load moves from %s: %s", filename, err)
        raise


def main() -> None:
    """Main function to execute game.

    :Description:
    - Main function to execute game.
    - Loads moves from moves.txt file.
    - Executes moves.
    - Saves final state to final_state.json.

    :Args:
    - `None`

    :Returns:
    - `None`

    :Raises:
    - `Exception`: If any error occurs during game execution

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
        moves: list[str] = load_moves(filename="moves.txt")

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

        with open(file="final_state.json", mode="w", encoding="utf-8") as file:
            json.dump(obj=final_state, fp=file, indent=4)
        logger.info(msg="Final state written to final_state.json")

    # pylint: disable=broad-exception-caught
    except Exception as err:  # noqa:BLE001
        logger.error("An error occurred during game execution: %s", err)


if __name__ == "__main__":
    main()
