from pathlib import Path

# digite no seu terminal para saber o caminho absoluto do seu projeto
# python -c 'import pathlib; print(pathlib.Path().absolute())'
ROOT_DIR = Path(__file__).parent
FILES_DIR = ROOT_DIR / "files"
WINDOW_ICON_PATH = FILES_DIR / "icon.png"

# Sizing
BIG_FONT_SIZE = 35
MEDIUM_FONT_SIZE = 24
SMALL_FONT_SIZE = 18
TEXT_MARGIN = 1
MINIMUM_WIDTH = 500

# Blue Colors
PRIMARY_COLOR = "#1e81b0"
DARKER_PRIMARY_COLOR = "#16658a"
DARKEST_PRIMARY_COLOR = "#115270"
