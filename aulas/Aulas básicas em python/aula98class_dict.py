# Dicionários em Python (tipo dict) 
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc. <--- classe
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list <--- classe

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}

pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda') #criando dicionário usando a classe

print(pessoa, type(pessoa))
print(pessoa['nome']) #retora o valor da chave "nome"
print(pessoa['sobrenome']) #a "chave" fica entre cochetes, como se estivesse indicando "índice"

print() #imprime nada

for chave in pessoa:
    print(chave, pessoa[chave]) # primeiro arg: "chave" - segundo arg: "valor da chave"