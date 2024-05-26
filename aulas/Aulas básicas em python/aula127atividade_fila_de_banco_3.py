#com duas filas
ultimo_fila1 = 10
fila1 = list(range(1, ultimo_fila1 + 1))
ultimo_fila2 = 20
fila2 = list(range(1, ultimo_fila2 + 1))

while True:
    print(f'\nExistem {len(fila1)} clientes na fila 1')
    print(f'Fila 1 atual: {fila1}')
    print(f'\nExistem {len(fila2)} clientes na fila 2')
    print(f'Fila 2 atual: {fila2}\n')

    print('Digite A para atendimento à fila 1,')
    print('B para atendimento à fila 2,')
    print('F para adicionar cliente na fila 1,')
    print('G para adicionar cliente na fila 2,')
    print('ou S para sair')

    operacoes = input('Operações (A, B, F, G ou S): ')

    # Verificação de entrada válida
    for char in operacoes:
        if char not in ['A', 'B', 'F', 'G', 'S']:
            print("Comando inválido! Digite 'A', 'B', 'F', 'G' ou 'S'")
            break
    else:
        for operacao in operacoes:
            if operacao == "F":
                ultimo_fila1 += 1
                fila1.append(ultimo_fila1)
            elif operacao == "G":
                ultimo_fila2 += 1
                fila2.append(ultimo_fila2)
            elif operacao == "A":
                if len(fila1) > 0:
                    atendido = fila1.pop(0)
                    print(f'Cliente {atendido} atendido na fila 1.')
                else:
                    print('Fila 1 vazia!')
            elif operacao == "B":
                if len(fila2) > 0:
                    atendido = fila2.pop(0)
                    print(f'Cliente {atendido} atendido na fila 2.')
                else:
                    print('Fila 2 vazia!')
            elif operacao == "S":
                break

    if 'S' in operacoes:
        print(f'\nExistem {len(fila1)} clientes na fila 1')
        print(f'Fila 1 atual: {fila1}')
        print(f'\nExistem {len(fila2)} clientes na fila 2')
        print(f'Fila 2 atual: {fila2}')
        break