# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3} -> se parece com dict, mas não tem chave e valor, apenas valor
# s1 = set('Luiz') -> retorna desordenado e cada letra se torna um valor
s1 = set()  # vazio obs.: {} -> é um dict
s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis naturalmente
# ex.: s1 = {1, 2, 3, 3, 3, 1}
# print(s1) -> {1, 2, 3}

# l1 = [1, 2, 3, 3, 3, 3, 3, 1] -> lista
# s1 = set(l1) -> lista -> set  s1 = {1, 2, 3}
# l2 = list(s1) -> set -> lista  l2 = [1, 2, 3]

# - não aceitam valores mutáveis;
# - seus valores serão sempre únicos;
# - não tem índices;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# s = {1, 2, 3}
# print(1 in s) -> True(bool)
# for i in s:
#     print(i) -> na ordem (normal)

# Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add('Luiz') # adc o valor
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4)) # se parece com o "add", precisa por em tupla para o valor nao quebrar
s1.clear() # limpa tudo
s1.discard('Olá mundo') # del o valor
s1.discard('Luiz')
print(s1)

# Operadores úteis:
# união (|) -  une sem repetição
# intersecção (&) - Itens presentes em ambos (intersection)
# diferença (-) - Itens presentes apenas no set da esquerda
# diferença simétrica (^) - Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 # une sem repetição
s3 = s1 & s2 # apenas os valores presente em ambos
s3 = s2 - s1 # ordem importa, o da esquerda é que será diminuido
s3 = s1 ^ s2 # apenas os valores não presente em ambos
print(s3)

# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('PARABÉNS')
        break

    print(letras)