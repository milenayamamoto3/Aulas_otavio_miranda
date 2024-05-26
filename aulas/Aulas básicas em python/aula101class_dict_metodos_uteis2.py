# copy - retorna uma cópia rasa (shallow copy)

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

d2 = d1 
d2['c1'] = 2
print(d1)
print(d2)
# d1 e d2 são cópias rasas de dicionários dependentes

d2 = d1.copy() # == d2 = copy.copy(d1) com o (import copy)
d2['c1'] = 9 #int é imutável, o int de d1 permanece com o valor
d2['l1'][0] = 1 #lista é mutável, a lista de d1 altera junto
print(d1)
print(d2)
# d1 e d2 ainda são cópias rasas, só os mutáveis continuam iguais ao alterar valor

import copy
d2 = copy.deepcopy(d1) 
d2['c1'] = 1000
d2['l1'][1] = 999999
print(d1)
print(d2) 
# d1 e d2 são cópias profundas, ou seja, a partir de momento que d2 pega a cópia de d1, 
# criou-se um dict separado (dicionário independente)

