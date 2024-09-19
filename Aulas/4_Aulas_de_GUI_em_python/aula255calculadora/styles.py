# QSS - Estilos do QT for Python
# https://doc.qt.io/qtforpython/tutorials/basictutorial/widgetstyling.html

# Dark Theme - How to use
# https://pyqtdarktheme.readthedocs.io/en/latest/how_to_use.html

import qdarktheme
from variables import DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR, PRIMARY_COLOR

# white color: #fff
# hover = pairar, passar o cursor encima sem clicar
# specialButton -> são os botões dos operadores
qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff; 
        background: {PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""


def setupTheme():
    qdarktheme.setup_theme(
        theme="dark",  # "light"
        corner_shape="rounded",  # "sharp"
        custom_colors={
            "[dark]": {
                "primary": f"{PRIMARY_COLOR}",  # cor primária do tema "dark"
            },
            "[light]": {
                "primary": f"{PRIMARY_COLOR}",
            },
        },
        additional_qss=qss,
    )
