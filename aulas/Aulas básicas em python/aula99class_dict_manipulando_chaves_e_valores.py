# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

pessoa['sobrenome'] = 'Miranda' #adicionando chave com valor no dict
print(pessoa)

chave = 'nome'
pessoa[chave] = 'Luiz Otávio'
print(pessoa[chave])

pessoa[chave] = 'Maria' #substituiu

del pessoa['sobrenome'] #deletou

print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome')) <--- por padrão, retorna "None" caso a chave não exita,
#se ela existir, retorna o valor da chave

if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

#outro modo de manipular o erro "keyError", é usando "Try e Except".
print(pessoa.get('sobrenome', 'Não existe')) # método "get" se existir, imprime(valor do 1º arg),
# se não existir, imprime(valor dado do 2º arg).