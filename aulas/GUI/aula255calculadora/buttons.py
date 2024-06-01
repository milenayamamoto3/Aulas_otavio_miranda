from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE
from utils import isEmpty, isNumOrDot, isValidNumber
from PySide6.QtCore import Slot

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from display import Display
    from info import Info


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
    def __init__(self, display: "Display", info: "Info", *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ["C", "◀", "^", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["", "0", ".", "="],
        ]

        self.display = display
        self.info = info
        # self.info.setText("Olá") # configura o texto da info
        self._equation = ""
        self._equationInitialValue = "Sua conta"
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        for rowNumber, rowData in enumerate(self._gridMask):
            for colNumber, buttonText in enumerate(rowData):
                button = Button(buttonText)

                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    # Define propriedade espicial
                    button.setProperty("cssClass", "specialButton")
                    self._configSpecialButton(button)

                self.addWidget(button, rowNumber, colNumber)

                slot = self._makeSlot(self._insertButtonTextToDisplay, button)

                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)  # type: ignore

    def _configSpecialButton(self, button):
        text = button.text()
        print("O texto do meu butão especial é :", text)

        if text == "C":
            self._connectButtonClicked(button, self._clear)

        if text in "-+/*":
            self._connectButtonClicked(
                button, self._makeSlot(self._operatorClicked, button)
            )

        if text in "=":
            self._connectButtonClicked(button, self._eq)

    def _makeSlot(self, func, *args, **kwargs):
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

    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()

    def _operatorClicked(self, button):
        buttonText = button.text()  # +-/* (etc...)
        displayText = self.display.text()  # Deverá ser meu número _left
        self.display.clear()  # Limpa o display

        # Se a pessoa clicou no operador sem
        # configurar qualquer número antes
        if not isValidNumber(displayText) and self._left is None:
            print("Não tem nada para colocar no valor da esquerda")
            return

        # Se houver algo no número da esquerda,
        # não fazemos nada. Aguardaremos o número da direita.
        if self._left is None:
            self._left = float(displayText)  # sincronizando o _left

        self._op = buttonText
        self.equation = f"{self._left} {self._op} ??"

        print(buttonText)

    def _eq(self):
        # como o display foi limpado, displayText = None
        displayText = self.display.text()

        if not isValidNumber(displayText):
            print("Sem nada para a direita")
            return

        self._right = float(displayText)
        self.equation = f"{self._left} {self._op} {self._right}"
        result = 0.0

        try:
            result = eval(self.equation)
        except ZeroDivisionError:
            print("Zero Division Error")

        self.display.clear()
        self.info.setText(f"{self.equation} = {result}")
        self._left = result
        self._right = None
