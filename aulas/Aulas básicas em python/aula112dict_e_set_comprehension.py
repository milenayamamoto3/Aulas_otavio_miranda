# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}
dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor #função "isinstance" de dois args(valor, class) 
    for chave, valor                      #considera apenas o valor da classe escolhida
    in produto.items()
    if chave != 'categoria'
}
print(dc) # criando uma nova dict a partir de outra dict

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]
dc = {
    chave: valor
    for chave, valor in lista
}
print(dc) # transformando a lista em dict

s1 = {2 ** i for i in range(10)}
print(s1) # criando uma set