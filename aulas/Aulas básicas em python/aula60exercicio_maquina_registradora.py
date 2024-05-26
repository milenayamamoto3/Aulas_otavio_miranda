
s = 0
while True:
    try:
        quantidade = int(input('Digite a quantidade: '))
        codigo = int(input('Digite o código do produto ou "0" para finalizar e ver a soma: '))
        if codigo == 0:
            break
        r = 0
        if codigo == 1:
            r = quantidade * 0.5
        elif codigo == 2:
            r = quantidade * 1
        elif codigo == 3:
            r = quantidade * 4
        elif codigo == 5:
            r = quantidade * 7
        elif codigo == 9:
            r = quantidade * 8
        else:
            print('Código inválido')
            continue
        s += r
    except:
        print('Digite um valor válido')    
print(f'Sua soma é {s:.2f}')