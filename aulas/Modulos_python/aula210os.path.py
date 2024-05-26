# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.
import os

#join -> grava o caminho apenas, não cria
caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
# print(caminho)

diretorio, arquivo = os.path.split(caminho)
# print(diretorio)
# print(arquivo)

nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
# print(nome_arquivo, extensao_arquivo)

# exists -> bool, True para existe o caminho, False para não existe
# print(os.path.exists('/Users/luizotavio/Desktop/curso-python-rep'))

# abspath -> caminho absoluto
# print(os.path.abspath('.'))

print(caminho)
print(os.path.basename(caminho)) #pega o último doc (arquivo.txt)
print(os.path.basename(diretorio)) #pega o último doc (curso)
print(os.path.dirname(caminho)) #pega o diretório sem o arquivo