# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()  #super está em detalhes(EXPLÍCITO)
#         print('DEPOIS DO UPPER')
#         return retorno

# string = MinhaString('Luiz')
# print(string.upper())

class A(object): #object EXPLÍCITO
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs): 
        # print('EI, burlei o sistema.')
        super().__init__(*args, **kwargs) #joga tudo para B

    def metodo(self):
        # super().metodo()  # B
        # super(B, self).metodo()  # A
        # super(A, self).metodo()  # object
        A.metodo(self) # super(A, self).metodo()
        B.metodo(self) # super(B, self).metodo()
        print('C')

# c = C()
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo() #Aqui, daria erro quando chegasse no super(A, self)
 #pois o objec de A não tem método
        
# print(C.mro()) #Method Resolution Order
# print(B.mro())
# print(A.mro())
        
c = C('Atributo', 'Qualquer')
# print(c.atributo)
# print(c.outra_coisa)

c.metodo()

