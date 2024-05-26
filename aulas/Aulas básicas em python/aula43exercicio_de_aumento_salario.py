try:
    salario = float(input('Digite seu salário: '))
    if salario > 1250.00:
        aumento = salario * 0.1
        total = salario + aumento
        print(f'Seu salário de R${salario:.2f} tem aumento de R${aumento:.2f} passando a ser R${total:.2f}')
    elif 0 <= salario <= 1250.00:
        aumento = salario * 0.15
        total = salario + aumento
        print(f'Seu salário de R${salario:.2f} tem aumento de R${aumento:.2f} passando a ser R${total:.2f}')
    else:
        print('Salário inválido. Digite um valor positivo.')

except ValueError:
    print('Digite apenas números válidos.')