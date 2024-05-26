# isinstance - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('STR')
        print(item.upper())

    elif isinstance(item, (int, float)): # OR 
        print('NUM')                     # True entra nesse bloco, pois "bool" é uma subclasse de "int"
        print(item, item * 2)            # Imprimirá 2, pois True é tratado como 1 em operações matemáticas.
    else:                                # E False tem valor de 0
        print('OUTRO')
        print(item)