"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
#duas maneiras do usuário conseguir apenas digitar NÚMEROS sem da erro!

numero_str = input(
    'Vou dobrar o número que vc digitar: '
)
#maneira 1 - usando try e except
try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

#maneira 2 - usando if e else com a função isdigit()

if numero_str.isdigit():
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
else:
    print('Isso não é um número')