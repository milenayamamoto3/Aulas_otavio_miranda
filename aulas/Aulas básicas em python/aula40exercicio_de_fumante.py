def calculo_de_dias_perdidos(cigarros_por_dia, anos_de_fumo):
    minutos_perdidos = 10
    dias_em_anos = 365

    total_cigarros = cigarros_por_dia * anos_de_fumo * dias_em_anos
    total_minutos = total_cigarros * minutos_perdidos

    total_de_dias = total_minutos / (24*60) #transformando minutos em dias

    return total_de_dias

def main():
    try:
        cigarros_por_dia = int(input('Quantos cigagros você fuma por dia? '))
        anos_de_fumo = int(input('Quantos anos fumando? '))

        total_de_dias = calculo_de_dias_perdidos(cigarros_por_dia, anos_de_fumo)

        print(f'Você já perdeu {total_de_dias:.0f} dias')

    except:
        print('Erro: Certifique-se de digitar valores numéricos inteiros válidos.')

if __name__ == "__main__":
    main()







