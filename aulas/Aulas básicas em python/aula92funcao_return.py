"""
Retorno de valores das funções (return)
"""
variavel = print('Luiz') # a função "print" é None, pois não há valor, ela apenas exibe o valor
print(variavel) # None

variavel = int('1') # int é uma classe
print(variavel) # retorna o valor inteiro

def soma(x, y):
    return x + y  # Return não tem nada a ver com o "print", ele valida.
                  #somente FUNÇÃO E MÉTODO tem o "return"
soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1 + soma2) # Aqui no print, as variáveis tem valor

def soma(x, y):
    if x > 10:
        return [10, 20] # o return na função retorna apenas 1
    return x + y        #e não esse outro ou vice-versa
soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11, 55))