# Battling Knights

A simulation of four knights battling for items on an 8x8 grid, moving in L-shapes (like a chess knight). See [Challenge.pdf](Challenge.pdf) for full rules.

## Setup

This project uses [uv](https://docs.astral.sh/uv/) for dependency management and requires Python 3.14+.

```bash
uv sync
```

## Usage

1. Edit [moves.txt](moves.txt) with moves you want to simulate (format described in [Challenge.pdf](Challenge.pdf)).
2. Run game:

    ```bash
    uv run main.py
    ```

3. Final state of all knights and items is written to `final_state.json`.

## Tests

```bash
uv run pytest
```
