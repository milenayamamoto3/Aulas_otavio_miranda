# Função para verificar se um número é primo
def is_prime(number):
    # Verificar se o número é igual a 0 ou 1
    if number <= 1:
        return False
    # Caso especial: 2 é primo
    elif number == 2:
        return True
    # Verificar se o número é par (exceto 2)
    elif number % 2 == 0:
        return False
    else:
        # Verificar divisibilidade por números ímpares a partir de 3
        for i in range(3, int(number**0.5) + 1, 2): #o número 3 é caso especial
            if number % i == 0:
                return False
        return True

# Solicitar entrada do usuário
try:
    num = int(input("Digite um número inteiro positivo: "))
    if is_prime(num):
        print(f"{num} é um número primo.")
    else:
        print(f"{num} não é um número primo.")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar um número inteiro positivo.")