from PySide6.QtWidgets import QPushButton
from variables import MEDIUM_FONT_SIZE


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        # self.setStyleSheet(f"font-size: {MEDIUM_FONT_SIZE}px;") -> sobresai
        font = self.font()  # especificando a fonte
        font.setPixelSize(MEDIUM_FONT_SIZE)
        # font.setItalic(True) -> itálico
        # font.setBold(True) -> negrito
        self.setFont(font)
        self.setMinimumSize(75, 75)  # largura, altura
        self.setProperty("cssClass", "specialButton")  # definiu propriedade
