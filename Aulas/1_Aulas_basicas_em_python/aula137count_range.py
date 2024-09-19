# count é um iterator sem fim (itertools)
from itertools import count  #precisa puxar o "count" de intertools

c1 = count(step=8, start=8) #nao tem fim
r1 = range(8, 100, 8) #tem fim

print('c1', hasattr(c1, '__iter__')) # True, é interável
print('c1', hasattr(c1, '__next__')) # True, é interator
print('r1', hasattr(r1, '__iter__')) # True, é interável
print('r1', hasattr(r1, '__next__')) # False, não é interator

print('count')
for i in c1:
    if i >= 100: #precisa usar o "if" para limite
        break

    print(i)
print()
print('range')
for i in r1:  #range não precisa de "if" para limite
    print(i)