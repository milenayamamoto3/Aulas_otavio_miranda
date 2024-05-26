# Função para verificar se um número é primo
def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(3, int(number**0.5) + 1, 2): #o número 3 é caso especial
            if number % i == 0:
                return False
        return True

# Solicitar entrada do usuário para obter o número de primos desejado (n)
try:
    n = int(input("Digite o número de primos que você deseja imprimir: "))
    count = 0  # Contador de números primos encontrados
    num = 2    # Começamos com o primeiro número primo (2)

    while count < n:
        if is_prime(num):
            print(num, end=" ") #argumento  da função print. Especificamente, end=" " define o que deve ser colocado após a impressão de cada número na mesma linha.
            count += 1
        num += 1

except ValueError:
    print("Entrada inválida. Certifique-se de digitar um número inteiro positivo para 'n'.")