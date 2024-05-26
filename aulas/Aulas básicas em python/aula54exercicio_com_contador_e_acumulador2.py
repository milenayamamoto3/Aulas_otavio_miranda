#calcula os valores de um depósito inicial e de cada mês com uma 
#taxa de juros mensal especificada ao longo de 24 meses.
x = 1
soma = 0
try:
    inicio = float(input('Qual seu depósito inicial? '))
    n = float(input('Qual a taxa de juros em porcentagem a.m.? '))
    while x <= 24: 
        if x == 1:
            soma = inicio + inicio*(n*10**-2)
        else:
            soma = soma + (soma * (n*10**-2))
        y = float(input(f'Seu total do mês {x} é R$ {soma:.2f}. Qual seu outro depósito? '))
        soma = soma + y    
        x += 1
except:
    print('Digite um número válido.')
print(f'Total em 24 meses é R${soma:.2f}')
