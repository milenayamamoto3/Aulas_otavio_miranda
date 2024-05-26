import sys #módulo

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [n for n in range(1000000)] # está na memória
generator = (n for n in range(1000000)) # não está na memória o valor desta função (generator)

print(sys.getsizeof(lista)) # mostra o tamanho da lista 
print(sys.getsizeof(generator)) # mostra o tamanho da função
print(generator)

# for n in generator:
#     print(n)