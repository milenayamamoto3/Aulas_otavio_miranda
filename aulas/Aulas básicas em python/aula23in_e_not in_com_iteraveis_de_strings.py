# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
# nome = 'Otávio'
# print(nome[2]) -> á
# print(nome[-4]) -> á
# print('vio' in nome) -> True
# print('zero' in nome) -> False
# print(10 * '-') > ----------
# print('vio' not in nome) -> False
# print('zero' not in nome) -> True

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')