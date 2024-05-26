# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

# def generator(n=0):
#    yield 1 #pausa
#    print("imprimindo...")
#    yield 2
#    print("mais uma vez...")
#    yield 3
#    print("vou terminar...")
#    return "ACABOU"
# gen = generator(n=0)
# print(gen.__iter__) #iterator de gen
# print(next(gen)) #pausa em yield 1
# print(next(gen)) #pausa em yield 2
# print(next(gen)) #pausa em yield 3
# print(next(gen)) #pausa em return dando erro

# def generator(n=0):
#    yield 1 #pausa
#    print("imprimindo...")
#    yield 2
#    print("mais uma vez...")
#    yield 3
#    print("vou terminar...")
#    return "ACABOU"
# gen = generator(n=0)
# for n in gen:
#     print(n) #nesse exemplo, não chega ao return dando erro

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n >= maximum:
            return
gen = generator(maximum=100) #aqui você controla os argumentos dos parâmetros
for n in gen: #aqui cada ciclo para no yield
    print(n)