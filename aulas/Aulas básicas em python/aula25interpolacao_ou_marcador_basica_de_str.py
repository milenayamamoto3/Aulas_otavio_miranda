"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (0123456789ABCDEF)
"""
nome = 'Luiz'
preco = 10000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %i é %08X' % (1500, 1500))
print('%9d' % preco) #sem o nº 0, considera-se o "espaço", como a variável é float
#e o marcador é inteiro, não dará erro, mas considerará a parte inteira do float
print('%-9d' % preco) #com o sinal negativo, a contagem de "espaço" inverterá de lado
