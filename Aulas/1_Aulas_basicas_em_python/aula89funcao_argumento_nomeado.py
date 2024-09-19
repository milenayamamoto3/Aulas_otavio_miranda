"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""
def oi(x, y):
    print(x + y)

print(oi) # local da função
print(oi(1, 2)) # primeiro ele executa o print da função e depois este print (None) por padrão

def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)

soma(1, 2, 3) # argumentos não nomeados 
soma(1, y=2, z=5) # argumentos nomeados(mas se nomear um, os seguintes precisam ser nomeados
#para não gerar erro)
print(1, 2, 3, sep='-') 