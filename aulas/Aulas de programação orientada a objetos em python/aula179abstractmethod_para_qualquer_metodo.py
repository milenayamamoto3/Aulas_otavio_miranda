# abstractmethod para qualquer método já decorado (@property e setter)
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.
from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):
        # A ordem dos atributos muda a saída
        # self.name = name # Se esse for primeiro, chama o setter
        # self._name = None # Implicitamente no property, o valor muda para None 
        self._name = None # Se esse for primeiro, implicitamente no property é None
        self.name = name # Depois nesse, o setter é chamado mudando o None para name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name): 
        self._name = name


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        # print('Sou inútil')

foo = Foo('Bar')
print(foo.name) # Aqui chama o property 