
#funções recursivas: se chamam de volta, resolve problemas grandes que 
    #podem ser quebrados, como fatorial (5*4*3*2*1=120)

#Ex 1
# def fatorial(n: int) -> int:
#     #Caso base, onde a função não faz mais recursão
#     if n == 1:
#         return 1
#     #Caso recursivo
#     return n * fatorial(n - 1)
# fat5 = fatorial(5)

# # import sys 
# # sys.setrecursionlimit(5000) #Aqui é perigoso, pois você pode ajustar o limit
# # fat1000 = fatorial(1000) # mil é o limite máximo, passou disso, erro

# print(fat5)

#Ex 2
# from collections import namedtuple
# from typing import List

# Caixa = namedtuple('Caixa', 'Tem_chave')

# def encontrar_chave(Caixas: List[Caixa], index: int = 0) -> Caixa:
#     #caso base
#     if len(Caixas) <= index:
#         return Caixa(False)
    
#     caixa = Caixas[index]

#     print(f'Buscando chave na caixa {index} -> {caixa}')

#     #caso base
#     if caixa.Tem_chave:
#         return Caixa
    
#     #caso recursivo
#     index += 1

#     return encontrar_chave(Caixas, index)
                     
# Caixas:  List[Caixa] = [
#     Caixa(False), Caixa(False), Caixa(False),
#     Caixa(False), Caixa(False), Caixa(False),
#     Caixa(False), Caixa(False), Caixa(False)
#     ]
# print(Caixas)
# print(encontrar_chave(Caixas))

