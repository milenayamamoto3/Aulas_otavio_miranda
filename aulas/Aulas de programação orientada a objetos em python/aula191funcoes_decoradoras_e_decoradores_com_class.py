# Funções decoradoras e decoradores com classes

def meu_repr(self): 
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr


def adiciona_repr(cls): #Função decoradora
    cls.__repr__ = meu_repr
    return cls


@adiciona_repr #Decorador
class Time:
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr #Decorador
class Planeta:
    def __init__(self, nome):
        self.nome = nome

# Time = adiciona_repr(Time)
brasil = Time('Brasil')
portugal = Time('Portugal')

# Planeta = adiciona_repr(Planeta)
terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)