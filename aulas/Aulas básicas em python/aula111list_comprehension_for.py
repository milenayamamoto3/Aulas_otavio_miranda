lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))

print(lista)

lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(lista)

lista = [
    [(x, letra) for letra in 'Luiz']   #essa lista é diferente
    for x in range(3)
]

print(lista)

# extra

string = 'Milena Manami'

nova_str = ''.join([letra for letra in string])
print(nova_str)

n_de_pulos_letras = 4
nova_str = '.'.join([string[i:i+2] for i in range(0, len(string), n_de_pulos_letras)])
print(nova_str)

# extra 2

nomes = ['Tulio', 'Maria']
nomes_nv = [nome.upper() for nome in nomes] # todos maiúsculos
print(nomes_nv)
nomes_nv = [nome.title() for nome in nomes] # só a primeira letra maiúscula
print(nomes_nv)
nomes_nv = [nome.lower() for nome in nomes] # todos minúsculos
print(nomes_nv)
nomes_nv = [f'{nome[:-1].lower()}{nome[-1].upper()}' for nome in nomes] # só a última letra maiúscula
print(nomes_nv)