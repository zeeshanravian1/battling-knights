# Battling Knights

## Name

Battling Knights

## Description

This project is built in [Python](https://www.python.org/) 3.12 with [Poetry](https://python-poetry.org/) for dependency management. This project is a simulation of a battle between two knights. The knights are placed on a 8x8 grid and can move in L shape.

## Installing Dependencies

### [Poetry](https://python-poetry.org/)

- This project uses Poetry for dependency management. You can follow this [tutorial](https://python-poetry.org/docs/#installation) to install Poetry on your system. Or you can follow below steps to install Poetry on your system.

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Add poetry to path:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

- Enable tab completion:

```bash
poetry completions bash >> ~/.bash_completion
```

- Restart your shell so the path changes take effect:

```bash
source ~/.bashrc
```

- Verify that poetry is installed properly by using this command:

```bash
poetry --version
```

- Update poetry version **(Optional)**:

```bash
poetry self update
```

- Create a new project:

```bash
poetry new <project_name>
```

> **_NOTE:_** Replace **< project_name >** with your project name.

- Create Virtual Environment:
Go to project directory and type following command in terminal.

```bash
poetry init
```

> **_NOTE:_** This command will ask you some questions, you can skip them by pressing enter key.

- Activate Virtual Environment:
To activate virtual environment type following command in terminal.

```bash
poetry shell
```

- Install Dependencies:
To install dependencies type following command in terminal.

```bash
poetry install
```

- Install Specific Dependency:
To install specific dependency type following command in terminal.

```bash
poetry add <dependency_name>
```

> **_NOTE:_** Replace **< dependency_name >** with your dependency name.

- Verify your environment dependencies by running:

```bash
poetry show
```

- Remove Dependency:
To remove dependency type following command in terminal.

```bash
poetry remove <dependency_name>
```

- Listing the environments associated with the project:
To show all virtual environments type following command in terminal.

```bash
poetry env list
```

- Remove Virtual Environment:
To remove virtual environment type following command in terminal.

```bash
poetry env remove <virtual_environment_name>
```

> **_NOTE:_** Replace **< virtual_environment_name >** with your virtual environment name.

- Update Dependencies:
To update dependencies type following command in terminal.

```bash
poetry update
```

- Deactivate Virtual Environment:
To deactivate virtual environment type following command in terminal.

```bash
exit
```

## Usage

- Install Dependencies:
To install dependencies type following command in terminal.

```bash
poetry install
```

- Edit the [moves.txt](moves.txt) file to contain the moves you want to make. For more information on the moves, see the [Challenge.pdf](Challenge.pdf) file.

- Run App:
To run the script type following command in terminal.

```bash
python main.py
```

- Output:
The output will be saved in [final_state.json](final_state.json) file.
