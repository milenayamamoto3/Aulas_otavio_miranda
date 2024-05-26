

# import sys
# sys.setrecursionlimit(1004) -> essa função é chamada para aumentar o limite de recursão

def recursiva(inicio=0, fim=4):
    print(inicio, fim)

    # Caso base
    if inicio >= fim:
        return fim

    # Caso recursivo
    # contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)

# print(recursiva(0, 1001)) -> parece o loop, até 1000 seria o limite de recursão 

def factorial(n):
    #caso base
    if n <= 1:
        return 1
    #caso recursivo
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(10))
print(factorial(100))