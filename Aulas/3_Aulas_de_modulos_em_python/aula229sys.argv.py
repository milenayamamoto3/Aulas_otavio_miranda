# sys.argv - Executando arquivos com argumentos no sistema
# Fonte = Fira Code
import sys

# Exemplo
# python aula229sys.argv.py "oi" "hello" "hi"
#             [0]            [1]   [2]    [3]

argumentos = sys.argv #lista
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Você não passou argumentos')
else:
    try:
        print(f'Você passou os argumentos {argumentos[1:]}')
        print(f'Faça alguma coisa com {argumentos[1]}')
        print(f'Faça outra coisa com {argumentos[2]}')
    except IndexError: #caso não tenha o argumento [2]
        print('Faltam argumentos')