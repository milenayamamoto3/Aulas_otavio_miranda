# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe
class A:
    def __new__(cls, *args, **kwargs): #se new não tem objct, ele retorna "None" e nem desce pro init
        print('Antes de criar a instância')
        instancia = super().__new__(cls)
        print('Depois')
        
        return instancia

    def __init__(self, x):
        self.x = x
        # print(self) #aqui chama o repr
        print('Sou o init') 

    def __repr__(self):
        return 'A()'
    
a = A(123) #saída __init__
# a = object.__new__(A)
# a.__init__() #saída __init__
print(a) #saída __repr__
print(a.x) #saída __new__