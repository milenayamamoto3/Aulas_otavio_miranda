"""
Higher Order Functions
Funções de primeira classe
"""
#função dentro de função

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args): # tupla
    return funcao(*args) # desempacotou a tupla


print(
    executa(saudacao, 'Bom dia', 'Luiz')
)
print(
    executa(saudacao, 'Boa noite', 'Maria')
)

#Termos técnicos: Higher Order Functions e First-Class Functions

#Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

#    Higher Order Functions - Funções que podem receber e/ou retornar outras funções

#    First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

#Não faria muita diferença no seu código, mas penso que deveria lhe informar isso.

#Observação: esses termos podem ser diferentes e ainda refletir o mesmo significado.