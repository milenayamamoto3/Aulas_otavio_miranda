# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec
import sys

from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QMainWindow,
    QPushButton,
    QWidget,
)

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle("Minha janela bonita")  # Add a title

botao1 = QPushButton("Botão 1")
botao1.setStyleSheet("font-size: 80px;")

botao2 = QPushButton("Botão 2")
botao2.setStyleSheet("font-size: 40px;")

botao3 = QPushButton("Botão 3")
botao3.setStyleSheet("font-size: 40px;")

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)


def slot_example(status_bar):
    status_bar.showMessage("O meu slot foi executado")
    print(123)  # printa no terminal


# statusBar
status_bar = window.statusBar()
status_bar.showMessage("Mostrar mensagem na barra")

# menuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu("Primeiro menu")
primeira_acao = primeiro_menu.addAction("Primeira ação")
primeira_acao.triggered.connect(  # type:ignore
    lambda: slot_example(status_bar)
)
# lambda é comumente usado para conectar sinais (como cliques em botões)
# a slots (métodos ou funções que respondem a esses sinais)
# de uma maneira mais concisa.

window.show()
app.exec()  # O loop da aplicação
