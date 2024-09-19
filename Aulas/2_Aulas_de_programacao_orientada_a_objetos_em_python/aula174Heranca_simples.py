# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived classclass Foo:

class Foo:   
    ...
help(Foo) #ajuda entender a class

class Pessoa:
    cpf = 'cpf pessoa'
    print('classe Pessoa')

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def falar_nome_class(self):
        print('método da classe Pessoa')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    print('classe Cliente')

    def falar_nome_class(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Aluno(Pessoa):
    print('classe Aluno')
    cpf = 'cpf aluno'

c1 = Cliente('Maria', 'Rosa')
c1.falar_nome_class()
a1 = Aluno('Luiz', 'Otávio')
a1.falar_nome_class()
# help(Cliente)
print(a1.cpf) # A ordem vem da class filha->class mãe->objct