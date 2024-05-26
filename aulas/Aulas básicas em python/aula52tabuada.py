def tabuada_multiplicacao(inicial, final, n):

    contador = inicial
    
    while contador <= final:
        resultado = n * contador
        print(f"{n} x {contador} = {resultado}")
        contador += 1

# Solicitar entrada do usuário com tratamento de erros
while True:
    try:
        numero_inicial = int(input("Digite o número inicial da tabuada: "))
        numero_final = int(input("Digite o número final da tabuada: "))
        n = int(input("Digite o número fixo para a multiplicação: "))
        
        if numero_inicial > numero_final:
            print("Erro: O número inicial não pode ser maior que o número final.")
        else:
            tabuada_multiplicacao(numero_inicial, numero_final, n)
            break
    except ValueError:
        print("Erro: Por favor, digite apenas números inteiros.")
