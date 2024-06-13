from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE
from utils import isEmpty, isNumOrDot, isValidNumber, converToNumber
from PySide6.QtCore import Slot
import math

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from display import Display
    from info import Info
    from main_window import MainWindow


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
    def __init__(
        self, display: "Display", info: "Info", window: "MainWindow", *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ["C", "D", "^", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["N", "0", ".", "="],
        ]

        self.display = display
        self.info = info
        self.window = window
        # self.info.setText("Olá") # configura o texto da info
        self._equation = ""
        self._equationInitialValue = "Sua conta aqui"
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
        self.display.eqPressed.connect(self._eq)
        self.display.delPressed.connect(self._backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self._confLeftOp)

        for rowNumber, rowData in enumerate(self._gridMask):
            for colNumber, buttonText in enumerate(rowData):
                button = Button(buttonText)

                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    # Define propriedade especial para operadores
                    button.setProperty("cssClass", "specialButton")
                    self._configSpecialButton(button)

                self.addWidget(button, rowNumber, colNumber)

                slot = self._makeSlot(self._insertToDisplay, buttonText)

                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)  # type: ignore

    def _configSpecialButton(self, button):
        text = button.text()

        if text == "C":
            self._connectButtonClicked(button, self._clear)

        if text == "D":
            self._connectButtonClicked(button, self.display.backspace)

        if text == "N":
            self._connectButtonClicked(button, self._invertNumber)

        if text in "-+/*^":
            self._connectButtonClicked(button, self._makeSlot(self._confLeftOp, text))

        if text == "=":
            self._connectButtonClicked(button, self._eq)

    @Slot()
    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):  # _ não vai usar a variável mas sabe que ela vem aqui
            func(*args, **kwargs)

        return realSlot

    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return

        number = converToNumber(displayText) * -1
        self.display.setText(str(number))

    @Slot()
    def _insertToDisplay(self, text):

        # Usando o eval para calcular no display
        # if buttonText == '=':
        #     self.display.setText(str(eval(self.display.text())))
        # else:
        #     self.display.insert(buttonText)

        newDisplayValue = self.display.text() + text

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(text)
        # self.display.setText(buttonText) -> cada click muda
        # print(buttonText) -> cada click mostra no terminal
        # self.display.clearFocus() # tira o cursor no display
        self.display.setFocus()

    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()
        self.display.setFocus()

    @Slot()
    def _confLeftOp(self, text):

        displayText = self.display.text()  # Deverá ser meu número _left
        self.display.clear()  # Limpa o display
        self.display.setFocus()

        # Se a pessoa clicou no operador sem
        # configurar qualquer número antes
        if not isValidNumber(displayText) and self._left is None:
            self._showError("Você não digitou nada.")
            return

        # Se houver algo no número da esquerda,
        # não fazemos nada. Aguardaremos o número da direita.
        if self._left is None:
            self._left = converToNumber(displayText)  # conf. o _left

        self._op = text
        self.equation = f"{self._left} {self._op} ??"

    @Slot()
    def _eq(self):
        # como o display foi limpado, displayText = None
        displayText = self.display.text()

        if not isValidNumber(displayText) or self._left is None:
            self._showError("Conta incompleta.")
            return

        self._right = converToNumber(displayText)  # conf. right
        self.equation = f"{self._left} {self._op} {self._right}"
        result = "error"

        try:
            # if "^" in self.equation:
            #     result = eval(self.equation.replace("^", "**"))
            if "^" in self.equation and isinstance(self._left, int | float):
                result = math.pow(self._left, self._right)
                result = converToNumber(str(result))
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._showError("Divisão por zero.")
        except OverflowError:
            self._showError("Essa conta não pode ser realizada.")

        self.display.clear()
        self.info.setText(f"{self.equation} = {result}")
        self._left = result
        self._right = None
        self.display.setFocus()

        if result == "error":
            self._left = None

    @Slot()
    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()  # focus no display

    def _makeDialog(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        return msgBox

    def _showError(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setInformativeText("Operação inválida")
        # msgBox.setIcon(msgBox.Icon.NoIcon)  # sem ícone
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()
        # msgBox.setStandardButtons(
        #     msgBox.StandardButton.ok
        #     | msgBox.button(msgBox.standardButton.NotoAll).setText("CANCEL")
        # )
        # result = msgBox.exec()  # executa

        # if result == msgBox.StandardButton.ok:
        #     print('Usuário clicou em "ok"')
        # elif result == msgBox.button(msgBox.standardButton.NotoAll).setText("CANCEL"):
        #     print('Usuário clicou em "CANCEL"')
        self.display.setFocus()

    def _showInfo(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()
        self.display.setFocus()
