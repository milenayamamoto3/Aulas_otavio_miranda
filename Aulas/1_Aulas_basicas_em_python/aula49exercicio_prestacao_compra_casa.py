def calcular_prestacao(valor_casa, salario, anos):
    meses = anos * 12
    prestacao_maxima = salario * 0.3
    prestacao = valor_casa / meses
    
    if prestacao <= prestacao_maxima:
        return prestacao
    else:
        return None

def main():
    try:
        valor_casa = float(input("Digite o valor da casa a comprar: "))
        salario = float(input("Digite o seu salário: "))
        anos = int(input("Digite a quantidade de anos a pagar: "))
    
        prestacao = calcular_prestacao(valor_casa, salario, anos)
    
        if prestacao is None:
            print("Desculpe, a prestação mensal excede 30% do seu salário.")
        else:
            print(f"O valor da prestação mensal é: R$ {prestacao:.2f}")
    except:
        print('Digite um número válido')

if __name__ == "__main__":
    main()