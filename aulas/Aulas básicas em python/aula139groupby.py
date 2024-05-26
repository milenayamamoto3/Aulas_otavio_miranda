# groupby - agrupando valores (itertools)
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def ordena(aluno): #função para ordenar os itens "aluno" pela sua chave "nota"
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena) #função sorted ordena a lista (cópia rasa)
#primeiro ordena usando a função sorted
grupos = groupby(alunos_agrupados, key=ordena) 
#segundo agrupa pelo valor da chave(nota)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)