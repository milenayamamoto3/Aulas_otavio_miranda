"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
texto = 'Luiz'  # iterável
#método 1
iteratador = iter(texto)  # iterator
while True:
     try:
         letra = next(iteratador)
         print(letra)
     except StopIteration:
         break

#método 2
for letra in texto:
    print(letra)