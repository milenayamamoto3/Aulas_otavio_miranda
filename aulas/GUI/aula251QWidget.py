# QWidget e QLayout de PySide6.QtWidgets
# QWidget -> genérico
# QLayout -> Um widget de layout que recebe outros widgets
import sys
from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget

app = QApplication(sys.argv)

botao = QPushButton("Botão 1")
botao.setStyleSheet("font-size: 80px;")

botao2 = QPushButton("Botão 2")
botao2.setStyleSheet("font-size: 40px;")

botao3 = QPushButton("Botão 3")
botao3.setStyleSheet("font-size: 40px;")

central_widget = QWidget()

layout = QGridLayout()
# QVBoxLayout -> botões na vertical
# QHBoxLayout -> botões na horizontal
# QGridLayout -> controlar os locais de cada botão
central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

"""
addWidget(widget, row, column, rowSpan, columnSpan)
widget: O widget que você deseja adicionar ao layout.
row: A linha na qual o widget será inserido. 
column: A coluna na qual o widget será inserido. 
rowSpan: O número de linhas que o widget deve abranger. 
columnSpan: O número de colunas que o widget deve abranger.
"""

central_widget.show()  # Central widget entre na hierarquia e mostre sua janela
app.exec()  # O loop da aplicação
