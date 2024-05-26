#calcula os valores de um depósito inicial com uma 
#taxa de juros mensal especificada ao longo de 24 meses.
x = 1
soma = 0
try:
    inicio = float(input('Qual seu depósito inicial? '))
    n = float(input('Qual a taxa de juros em porcentagem a.m.? '))
    while x <= 24: 
        if x == 1:
            soma = inicio + inicio*(n*10**-2)
            print(f'Seu total do mês {x} é R$ {soma:.2f}')
        else:
            soma = soma + (soma * (n*10**-2))
            print(f'Seu total do mês {x} é R$ {soma:.2f}')
        x += 1
except:
    print('Digite um número válido.')
print(f'Total em 24 meses é R${soma:.2f}')
