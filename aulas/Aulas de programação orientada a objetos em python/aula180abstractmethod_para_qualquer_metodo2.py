from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None 
        self.name = name 

    @property
    @staticmethod
    def name(self): ...

class Foo(AbstractFoo):
    name = '' # da atributo para classe Foo ao em vez do property, que é um método 
 #que se comporta como atributo
    def __init__(self, name):
        super().__init__(name)
        # print('Sou inútil')

foo = Foo('Bar')
print(foo.name) 