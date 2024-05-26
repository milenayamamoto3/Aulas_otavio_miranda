# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 4

def multiplicador(multiplicadora):
    def multiplicar(numero):
        return numero * multiplicadora
    return multiplicar 

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)

print(duplicar) #sem o argumento do parâmetro da função interna, ele retorna "multiplicar" mostrando local da memória
print(triplicar(2))    
print(quadruplicar(2))