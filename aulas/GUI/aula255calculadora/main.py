import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH
from display import Display
from info import Info
from styles import setupTheme
from buttons import Button

if __name__ == "__main__":
    # nomenclaturas:
    # snake_case
    # PascalCase
    # camelCase

    # Cria a aplicação com tema
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info("2.0 ^ 10.0 = 1024")
    window.addToVLayout(info)

    # Display
    display = Display()  # if u put a text inside, it will be printed
    display.setPlaceholderText("Digite aqui")  # fica transparente
    window.addToVLayout(display)

    button = Button("Texto do botão")
    window.addToVLayout(button)

    button2 = Button("Texto do botão")
    window.addToVLayout(button2)

    # Exemplo de addWidget com QLabel
    # label1 = QLabel("O meu texto")
    # label1.setStyleSheet("font-size: 150px;")
    # window.addToVLayout(label1)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
