def calcular_multa(velocidade):
    limite_velocidade = 80
    valor_multa_por_km = 5
    km_acima_limite = velocidade - limite_velocidade

    if km_acima_limite <= 0:
        print("Parabéns! Você está dentro do limite de velocidade.")
    else:
        valor_multa = km_acima_limite * valor_multa_por_km
        print(f"Você foi multado por exceder o limite de velocidade em {km_acima_limite} km/h.")
        print(f"O valor da multa é de R$ {valor_multa:.2f}.")

def main():
    try:
        velocidade = float(input("Digite a velocidade do carro (em km/h): "))
        calcular_multa(velocidade)
    except ValueError:
        print("Por favor, digite um valor numérico válido para a velocidade.")

if __name__ == "__main__":
    main()