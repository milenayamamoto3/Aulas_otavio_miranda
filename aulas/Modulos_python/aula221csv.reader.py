# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula220csv_exemplo.csv'

# with open(CAMINHO_CSV, 'r', encoding='utf8') as arquivo:
#     leitor = csv.reader(arquivo)
    # next(leitor) # pula a primeira linha (linha da coluna neste caso)

    # print(next(leitor)) # se o next anterior tiver comentado, imprime a primeira linha

    # for linha in leitor:
    #     print(linha[0]) # imprime a coluna "nome" com seus valores

with open(CAMINHO_CSV, 'r', encoding='utf8') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha)
        print(linha['Nome'], linha['Idade'], linha['Endereço'])