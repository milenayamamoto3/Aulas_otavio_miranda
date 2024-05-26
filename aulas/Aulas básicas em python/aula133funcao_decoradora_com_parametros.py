# Decoradores com parâmetros
def fabrica_de_decoradores(a=None, b=None, c=None): #parâmetros da decoradora, "None" 
                                                    #como padrão
    def fabrica_de_funcoes(func): #decoradora de função
        print('Decoradora 1')

        def aninhada(*args, **kwargs): #troca pela função "soma"
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes

@fabrica_de_decoradores(1, 2, 3) #com parâmetros
def soma(x, y):
    return x + y

decoradora = fabrica_de_decoradores() #sem parâmetros
multiplica = decoradora(lambda x, y: x * y) #lambda é função anônima 
                                            #(lambda argumentos: expressão)
dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)