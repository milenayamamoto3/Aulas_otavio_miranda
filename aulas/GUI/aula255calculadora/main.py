import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH
from display import Display
from info import Info
from styles import setupTheme
from buttons import Button, ButtonsGrid

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
    window.addWidgetToVLayout(info)

    # Display
    display = Display()  # if u put a text inside, it will be printed
    display.setPlaceholderText("Digite aqui")  # fica transparente
    window.addWidgetToVLayout(display)

    # Grid (Adicionando o layout ButtonsGrid para o layout vLayout)
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Exemplo de addWidget ao vLayout com QPushButton (Button)
    # button = Button("Texto do botão")
    # window.addWidgetToVLayout(button)

    # Exemplo de addWidget com QLabel
    # label1 = QLabel("O meu texto")
    # label1.setStyleSheet("font-size: 150px;")
    # window.addWidgetToVLayout(label1)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
