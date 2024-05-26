# map, partial, GeneratorType e esgotamento de Iterators

from functools import partial
from types import GeneratorType

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

#partial: função que cria funções parciais de funções existentes
aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)
#maneira comprehension:
# novos_produtos = [
#     {**p,
#         'preco': aumentar_dez_porcento(p['preco'])}
#     for p in produtos
# ]

#maneira map:
def muda_preco_de_produtos(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(
            produto['preco']
        )
    }
    #map(função, iterável) -> aplica a função em cada item do iterável retornando 
novos_produtos = list(map(                  #um iterator
    muda_preco_de_produtos,
    produtos
))

print_iter(produtos)
print_iter(novos_produtos)

#list(map), map
print(novos_produtos) #retorna uma lista, iterator
print(hasattr(novos_produtos, '__iter__')) # True, True
print(hasattr(novos_produtos, '__next__')) # False, True

#GeneratorType
novos_produtos = (x for x in produtos)
print(isinstance(novos_produtos, GeneratorType)) #True, pois mudou "novos_produtos"
              #para um generator

#exemplo de usar map:
print(
    list(map(
        lambda x: x * 3,
        [1, 2, 3, 4]
    ))
)

#esgotamento de iterators:
print(list(novos_produtos)) #na linha 42, o map já está como lista, então esta função
#dará certo. Caso ao contrário, retornaria uma lista vazia, pois iterator é esgotável