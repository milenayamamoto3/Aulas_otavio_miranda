# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b) -> 2 1

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}
# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2) -> nome Aline
# print(b1, b2) -> sobrenome Souza

# for chave, valor in pessoa.items():
#     print(chave, valor) -> nome Aline
#                            sobrenome Souza

# pessoas_completa = {**pessoa, 'nome':'Brenda'} -> alterando a chave "nome"
# pessoas_completa = {**pessoa, 'apelido':'Japa'} -> adicionando nova chave com valor
pessoas_completa = {**pessoa, **dados_pessoa} # concatenando dois dict 
# print(pessoas_completa) -> {'nome': 'Aline', 'sobrenome': 'Souza', 'idade': 16, 'altura': 1.6}

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs): #kwargs sempre usa (**) ao usá-lo
    print('NÃO NOMEADOS:', args) #imprime "()" na 1º chamada e "(1, 2)" na 2º
    print(kwargs)

mostro_argumentos_nomeados(nome='Joana', qlq=123) #argumentos nomeados
mostro_argumentos_nomeados(1, 2, nome='Joana', qlq=123) #argumentos n nomeados e nomeados
mostro_argumentos_nomeados(**pessoas_completa) # desempacotando todos os itens

