"""
id = Identidade
None = Não valor
is e is not - é e não é (tipo, valor, identidade)
"""
#variáveis com o mesmo valor de objeto, 
#suas id são iguais. Caso contrário, seriam diferentes.
v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2))

#usando is e is not com None.
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')