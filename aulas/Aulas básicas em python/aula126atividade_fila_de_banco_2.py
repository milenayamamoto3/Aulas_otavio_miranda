#usando várioas comandos
ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print(f'\nExistem {len(fila)} clientes na fila')
    print(f'Fila atual: {fila}')
    print('Digite F para adicionar um cliente ao fim da fila,')
    print('ou A para realizar o atendimento. S para sair')
    operacoes = input('Operações (F, A ou S): ')

    # Verificação de entrada válida
    for char in operacoes:
        if char not in ['A', 'F', 'S']:
            print("Comando inválido! Digite 'A', 'F' ou 'S'")
            break
    else:
        for operacao in operacoes:
            if operacao == "A":
                if len(fila) > 0:
                    atendido = fila.pop(0)
                    print(f'Cliente {atendido} atendido.')
                else:
                    print('Fila vazia!')
            elif operacao == "F":
                ultimo += 1  # Incrementa o ticket do novo cliente
                fila.append(ultimo)
            elif operacao == "S":
                break

    if 'S' in operacoes:
        print(f'\nExistem {len(fila)} clientes na fila')
        print(f'Fila atual: {fila}')
        break