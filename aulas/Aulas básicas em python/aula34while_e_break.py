"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
condicao = True
# while condicao:
#     print(1)
#esse código acima é o que chamamos de loop infinito, pois não tem fim.
#no terminal, digite ctrl+c para finalizar.
while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')