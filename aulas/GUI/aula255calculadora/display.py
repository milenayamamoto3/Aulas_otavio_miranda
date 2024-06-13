from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QKeyEvent
from variables import BIG_FONT_SIZE, MINIMUM_WIDTH, TEXT_MARGIN
from utils import isEmpty, isNumOrDot


class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

        # self.setReadOnly(True)  # não deixa o usuário clicar em seu teclado

    def configStyle(self):
        margins = [
            TEXT_MARGIN for _ in range(4)
        ]  # [TEXT_MARGIN, TEXT_MARGIN, TEXT_MARGIN, TEXT_MARGIN] -> left, top, right, bottom
        self.setStyleSheet(f"font-size: {BIG_FONT_SIZE}px;")  # tamanho das letras
        self.setMinimumHeight(BIG_FONT_SIZE * 2)  # altura min
        self.setMinimumWidth(MINIMUM_WIDTH)  # largura min
        self.setAlignment(Qt.AlignmentFlag.AlignRight)  # cursor para a direita
        self.setTextMargins(*margins)  # asterisco tira da lista

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()  # strip remove espaços dos lados
        key = event.key()  # tecla
        KEYS = Qt.Key

        # print(event.text())  # valor digitado
        # print(event.key())  # código do valor digitado

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]
        isOperator = key in [
            KEYS.Key_Plus,
            KEYS.Key_Minus,
            KEYS.Key_Slash,
            KEYS.Key_Asterisk,
            KEYS.Key_P,
        ]

        if isEnter:
            print(f"Enter {text} pressionado, sinal emitido", type(self).__name__)
            self.eqPressed.emit()
            return event.ignore()  # fazer nada com o enter
        # return super().keyPressEvent(event)
        if isDelete:
            print(f"Delete {text} pressionado, sinal emitido", type(self).__name__)
            self.delPressed.emit()
            return event.ignore()

        if isEsc:
            print(f"Escape {text} pressionado, sinal emitido", type(self).__name__)
            self.clearPressed.emit()
            return event.ignore()

        if isOperator:
            if text.lower() == "p":
                text = "^"
            print(
                f"OperadorPressed {text} pressionado, sinal emitido",
                type(self).__name__,
            )
            self.operatorPressed.emit(text)
            return event.ignore()

        # Não passar daqui se não tiver texto
        if isEmpty(text):
            return event.ignore()

        if isNumOrDot(text):
            print(
                f"inputPressed {text} pressionado, sinal emitido", type(self).__name__
            )

            self.inputPressed.emit(text)
            return event.ignore()
