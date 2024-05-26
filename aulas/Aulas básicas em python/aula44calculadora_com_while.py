""" Calculadora com while """
while True:
    print('nummmmm')
    sair = input('Quer sair? [s]im: ').lower().startswith('s') ##startswith é boolean

    if sair is True:
        break