"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

def soma(*args):
    total = 0
    for numero in args:
        print('Total', total, numero)
        total += numero
        print('Total', total)
soma(1, 2, 3, 4, 5)

def somaa(*args):
    total = 0
    for numero in args:
        total += numero
    return total
somaa_total = somaa(1, 2, 3)
print(somaa_total)

print(sum((1, 2, 3, 4, 5))) #função sum só aceita até 2 argumentos iteráveis numéricos
#a função sum tem apenas 1 arg, a tupla acima é iterável contendo apenas números 

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10 #tupla

outra_soma = somaa(*numeros) #desempacotou a tupla para virar argumentos na função somaa
print(outra_soma)

print(sum(numeros))
print(*numeros) #printando o desempacotamento da tupla