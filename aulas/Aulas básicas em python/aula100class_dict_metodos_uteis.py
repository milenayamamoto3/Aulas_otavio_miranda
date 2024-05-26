# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 900,
    'sobrenome': 'Sol',
}

print(len(pessoa)) # era pra ser 4, mas como tem chave repetida, ele desconsidera o que foi subst

print(list(pessoa.keys())) # cria lista do dict "pessoa" com o método "keys" pegando as CHAVES
print(list(pessoa)) # cria lista do dict "pessoa" do mesmo jeito sem o método "keys"

print(list(pessoa.values())) # cria lista do dict "pessoa" com o método "values" pegando VALORES

print(list(pessoa.items())) # cria lista do dict "pessoa" com o método "items" pegando 
#tuplas contendo CHAVE e VALOR

print(pessoa.items()) # retorna dict_items([('nome', 'Luiz Otávio'), ('sobrenome', 'Sol'), ('idade', 900)])

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa.setdefault('idade', 0) # método para retorna "0" caso a chave "idade" não exista, mas 
#como ela existe, retorna o valor 
print(pessoa['idade'])



