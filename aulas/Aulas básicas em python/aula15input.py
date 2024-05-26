# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}')
#mostrando o nome e o valor da variável:
# print(f'O seu nome é {nome=}')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')
#se nos input o usuário colocar números, a soma do f-strings dará certo.
#se o usuário colocar letras, dará erro, pois não tem como transformar uma letra em inteiro.
