import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH

if __name__ == "__main__":
    # Cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Exemplo de addWidget com QLabel
    label1 = QLabel("O meu texto")
    label1.setStyleSheet("font-size: 150px;")
    window.addWidgetToVLayout(label1)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
