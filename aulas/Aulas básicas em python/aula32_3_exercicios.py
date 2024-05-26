"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
#resolução 1:
digite_um_numero_inteiro = input('Digite um número inteiro: ')
try: 
    numero_inteiro = int(digite_um_numero_inteiro)
    if numero_inteiro % 2 == 0:
        print('Seu número é par')
    if numero_inteiro % 2 != 0:
        print('Seu número é ímpar')
except:
    print('Não é um número inteiro')

#resolução 2:
num_int = input('Digite um número inteiro: ')
if num_int.isdigit():
    num_int_int = int(num_int)
    if num_int_int % 2 == 0:
        print('Seu número é par.')
    else:
        print('Seu número é ímpar.')
else:
    print('Não é um número inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = input('Qual o horário agora? Digite apenas a HORA SEM OS MINUTOS ')
if horario.isdigit():
    horario_int = int(horario)
    if horario_int >= 0 and horario_int <= 11:
        print('Bom Dia!')
    elif horario_int >= 12 and horario_int <= 17:
        print('Boa Tarde!')
    elif horario_int >= 18 and horario_int <= 23:
        print('Boa Noite!')
    else:
        print('Não conheço essa hora')
else:
    print('Digite números inteiros apenas.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Qual seu primeiro nome? ')
if nome:
    if len(nome) <= 4:
        print('Seu nome é curto') 
    elif len(nome) >= 5 and len(nome) <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite algo.')





