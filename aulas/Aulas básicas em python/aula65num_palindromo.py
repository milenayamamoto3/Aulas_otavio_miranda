def is_palindrome(number):
    # Converte o número em uma string para facilitar a manipulação dos caracteres
    num_str = str(number)
    
    # Compara a string original com a sua reversa
    return num_str == num_str[::-1] #pega do final ao início recuando

try:
    num = int(input("Digite um número: "))
    
    if is_palindrome(num):
        print(f"{num} é um número palíndromo.")
    else:
        print(f"{num} não é um número palíndromo.")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar um número inteiro.")