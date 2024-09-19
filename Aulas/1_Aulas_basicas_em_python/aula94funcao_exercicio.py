def multi(*args):  #total da multiplicação usando função de argumentos não nomeados
    total = 1
    for numero in args:
        total *= numero
    return total
    
print(multi(1, 33, 55, 786, 88))

def par_impar(x):  #return sendo usado como se fosse string e o uso dele sem o else.
    if x % 2 == 0:
        return f'{x} é par'
    return f'{x} é ímpar'
      
print(par_impar(3))