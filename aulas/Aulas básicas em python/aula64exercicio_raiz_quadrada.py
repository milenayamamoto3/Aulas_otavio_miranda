def calcular_raiz_quadrada(n):
    b = 2  # Valor inicial para a base b
    p = (b + (n / b)) / 2  # Valor inicial para p

    while abs(n - p**2) >= 0.0001:  #abs = função que retorna valor absoluto (positivo)
        b = p
        p = (b + (n / b)) / 2

    return p

try:
    n = float(input("Digite um número para calcular a raiz quadrada: "))
    if n < 0:
        print("A raiz quadrada de um número negativo não é real.")
    else:
        resultado = calcular_raiz_quadrada(n)
        print(f"A raiz quadrada de {n} é aproximadamente {resultado:.4f}")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar um número válido.")