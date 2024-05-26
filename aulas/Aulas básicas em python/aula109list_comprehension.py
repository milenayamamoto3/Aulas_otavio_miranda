# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

print(list(range(10))) # lista de 0 a 10 (maneira1)

lista = [] # lista de 0 a 10 (maneira2)
for numero in range(10):
    lista.append(numero)
print(lista)

lista = [numero for numero in range(10)] # lista de 0 a 10 (maneira3)
print(lista)

lista = [              # lista de 0 a 10 sendo multiplicado por 2
    numero * 2
    for numero in range(10)
]
print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}  #o que vem na esquerda do "for" é mapeamento
    for produto in produtos
] # ** -> para dict

print(novos_produtos)
print(*novos_produtos, sep='\n') # * -> para list