""" Calculadora com while """
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    numero_valido = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numero_valido = True

    except:
        numero_valido = None

    if numero_valido is None:
        print('Um ou ambos números digitados são inválidos')
        continue

    operador = input('Digite um operador (+-/*): ')
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta. Confira abaixo:')

    if operador == '+':
        print(f'{num_1_float}+{num_2_float}=', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float}-{num_2_float}=', num_1_float - num_2_float)
    elif operador == '*':
        print(f'{num_1_float}*{num_2_float}=', num_1_float * num_2_float)
    elif operador == "/":
        print(f'{num_1_float}/{num_2_float}=', num_1_float / num_2_float)
    else:
        print('Nunca deveria ter chegar aqui')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break