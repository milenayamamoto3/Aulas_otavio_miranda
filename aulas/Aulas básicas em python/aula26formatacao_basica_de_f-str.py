"""
Formatação básica de strings
s - string
d e i - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
b - Binário
o - Octal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal -  + -> "+" e -- -> "-"
= - Força o número a aparecer antes dos zeros
Ex.: 0>-100,.1f / 0=+10,.1f
Conversion flags - !r !s !a 
!r - repr() -  representação bruta do objeto
!s - str() - usado para obter a representação em formato de string de um objeto
!a - ASCII (repr with quotes and escape non-ASCII characters) - usado para obter a 
representação de um objeto em formato ASCII, com aspas e caracteres não ASCII escapados.
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{variavel:&^10}.')
print(f'{1000.4873648123746:0>-100,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}') 
print(f'{variavel!s}')