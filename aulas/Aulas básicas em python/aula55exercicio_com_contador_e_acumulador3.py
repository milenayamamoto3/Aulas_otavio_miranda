#Pergunte ao usuário o valor inicial da dívida, juros mensais e valor mensal que será pago
#Imprima número de vezes que a dívida será paga, total pago e total de juros.
try:
    divida_inicial = float(input('Qual o valor inicial da dívida? '))
    juro_mensal = float(input('Qual o juro mensal em porcentagem? '))
    pagamento_mensal = float(input('Qual o valor mensal a ser pago? '))

    meses = 0
    total_pago = 0
    total_juros_pago = 0

    while divida_inicial > 0:
        juros = divida_inicial * (juro_mensal * 0.01) 
        divida_inicial += juros - pagamento_mensal  # Subtrai o pagamento mensal e acrescenta juros
        total_pago += pagamento_mensal
        total_juros_pago += juros
        meses += 1

    print(f'Número de meses para pagar a dívida: {meses}')
    print(f'Total pago: R$ {total_pago:.2f}')
    print(f'Total de juros pago: R$ {total_juros_pago:.2f}')

except ValueError:
    print('Digite valores válidos para as entradas.')