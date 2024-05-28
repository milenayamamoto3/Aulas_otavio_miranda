from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE
from utils import isEmpty, isNumOrDot, isValidNumber
from display import Display
from PySide6.QtCore import Slot


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
        # self.setCheckable(True) # check on/off


class ButtonsGrid(QGridLayout):
    def __init__(self, display: Display, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ["C", "◀", "^", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["", "0", ".", "="],
        ]

        self.display = display
        self._makeGrid()

    def _makeGrid(self):
        for rowNumber, rowData in enumerate(self._gridMask):
            for colNumber, buttonText in enumerate(rowData):
                button = Button(buttonText)

                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    # Define propriedade espicial
                    button.setProperty("cssClass", "specialButton")

                self.addWidget(button, rowNumber, colNumber)

                buttonSlot = self._makeButtonDisplaySlot(
                    self._insertButtonTextToDisplay,
                    button,
                )
                button.clicked.connect(buttonSlot)  # type: ignore

    def _makeButtonDisplaySlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):  # _ não vai usar a variável mas sabe que ela vem aqui
            func(*args, **kwargs)

        return realSlot

    def _insertButtonTextToDisplay(self, button):
        buttonText = button.text()

        # Usando o eval para calcular no display
        # if buttonText == '=':
        #     self.display.setText(str(eval(self.display.text())))
        # else:
        #     self.display.insert(buttonText)

        newDisplayValue = self.display.text() + buttonText

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(buttonText)
        # self.display.setText(buttonText) -> cada click muda
        # print(buttonText) -> cada click mostra no terminal
