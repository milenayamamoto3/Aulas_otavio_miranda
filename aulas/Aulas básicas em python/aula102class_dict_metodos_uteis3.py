# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}

# nome = p1.pop('nome')
# print(nome) #imprime o valor da chave deletada
# print(p1) #dict atualizado sem a chave deletada

# ultima_chave = p1.popitem() # se colocar valor dentro deste (), dará erro
# print(ultima_chave) # retora uma tupla com a última chave com seu valor
# print(p1) #dict atualizado sem a última chave

#p1.update({                       -> por meio de dicionário
#    'nome': 'novo valor',         -> atualizando
#    'idade': 30,                  -> adicionando
#})
#print(p1)

# p1.update(nome='novo valor', idade=30)  -> por meio de parâmetros nomeados
# print(p1)

# tupla = ('nome', 'novo valor'), ('idade', 30) -> por meio de tupla
# p1.update(tupla)
# print(p1)

# lista = ['nome', 'novo valor'], ['idade', 30] -> por meio de lista
# p1.update(lista)
# print(p1)