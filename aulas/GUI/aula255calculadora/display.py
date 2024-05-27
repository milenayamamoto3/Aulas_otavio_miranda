from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONT_SIZE, MINIMUM_WIDTH, TEXT_MARGIN


class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [
            TEXT_MARGIN for _ in range(4)
        ]  # [TEXT_MARGIN, TEXT_MARGIN, TEXT_MARGIN, TEXT_MARGIN] -> left, top, right, bottom
        self.setStyleSheet(f"font-size: {BIG_FONT_SIZE}px;")  # tamanho das letras
        self.setMinimumHeight(BIG_FONT_SIZE * 2)  # altura min
        self.setMinimumWidth(MINIMUM_WIDTH)  # largura min
        self.setAlignment(Qt.AlignmentFlag.AlignRight)  # cursor para a direita
        self.setTextMargins(*margins)  # asterisco tira da lista
