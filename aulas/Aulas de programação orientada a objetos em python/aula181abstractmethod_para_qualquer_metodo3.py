from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None 
        self.name = name 

    @property
    def name(self): 
        return self._name
    
    @name.setter
    @staticmethod
    def name(self, name): ...

class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        # print('Sou inútil')
    
    @AbstractFoo.name.setter  # chamou o name da classe mãe
    def name(self, name): 
        self._name = name

foo = Foo('Bar')
print(foo.name) 