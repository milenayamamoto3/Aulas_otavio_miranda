# juntar as duas listas até o último índice da lista menor
# Resultado:
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

def zipper(l1, l2):
    intervalo = min(len(l1), len(l2)) #min é uma função que pega o menor da lista
    return [(l1[i], l2[i]) for i in range(intervalo)]
print(zipper(l1, l2))

from itertools import zip_longest

print(list(zip(l1, l2))) #já existe a função zip em python
print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE'))) #zip_longest vai até o
                 #último índice da lista maior