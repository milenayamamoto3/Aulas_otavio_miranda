"""
split e join com list e str
split - divide uma string formando uma lista
join - une uma string
strip - tira os espaços vazios tanto da direita, como da esquerda
lstrip - tira os espaços vazios da esquerda
rstrip - tira os espaços vazios da direita
"""
frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases_cruas)
print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)