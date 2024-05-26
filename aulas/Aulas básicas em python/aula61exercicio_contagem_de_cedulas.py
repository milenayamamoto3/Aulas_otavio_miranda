while True:
    try:
        cedulas = 0
        atual = 100
        valor = int(input('Digite o valor a pagar: '))
        if valor == 0:
            print('Digite um valor acima de "0"')
            continue
        while True:  
            if atual <= valor:
                valor -= atual
                cedulas += 1
            else:
                print(f'{cedulas} cédula(s) de R${atual}')
                if valor == 0:
                    break
                if atual == 100:
                    atual = 50
                elif atual == 50:
                    atual = 20
                elif atual == 20:
                    atual = 10
                elif atual == 10:
                    atual = 5
                elif atual == 5:
                    atual = 1
                cedulas = 0
        sair = input('Deseja [s]air? ').lower()
        if sair == 's':
            break
    except:
        print('Digite um número válido')
           