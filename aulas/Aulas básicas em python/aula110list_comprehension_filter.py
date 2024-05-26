# Filtro em list comprehension (filter)
import pprint #pretty print

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)
#sort_dicts -> ordenamento de chaves
#width -> largura de linha (até 40 caracters)

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

print(novos_produtos)
p(novos_produtos)

lista = [n for n in range(10) if n < 5] # é filter "if n < 5" tudo que vai na direita do for
print(lista)

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}  #altera valor 
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10  #seleciona quem vai imprimir
]
p(novos_produtos)