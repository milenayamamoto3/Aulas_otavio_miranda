# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.

# lista = [4, 32, 1, 34, 5, 6, 6, 21]
# lista.sort()  -> ordenação 
# sorted(lista) -> ordenação (cópia rasa da lista)
# lista.sort(reverse=True) -> ordenação invertida
# print(lista)

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

#maneira 1:
def ordena(item):
    return item['nome'] # chave escolhida é o que será ordenado através pelo UTF-8

lista.sort(key=ordena)

for item in lista:
    print(item)

#maneira 2 (usando lambda):
lista.sort(key=lambda item: item['nome'])
for item in lista:
    print(item)

#maneira 3:
def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome']) # l1 é a cópia rasa da lista ordenado pelo "nome"
l2 = sorted(lista, key=lambda item: item['sobrenome']) # l2 é a cópia rasa da lista ordenado pelo "sobrenome"

exibir(l1)
exibir(l2)