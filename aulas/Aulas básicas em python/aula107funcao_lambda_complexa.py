def executa(funcao, *args): #função padrão
    return funcao(*args)

def soma(x, y): #função 1
    return x + y

# 3 maneiras:
print(
    executa(
        lambda x, y: x + y,
        2, 3
    ), executa(soma, 2, 3),
    soma(2, 3)
)

def cria_multiplicador(multiplicador): #função 2
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

# 2 maneiras:
duplica1 = cria_multiplicador(2)
#ou
duplica2 = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica1(2))
print(duplica2(2))

# exemplo extra:
print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)