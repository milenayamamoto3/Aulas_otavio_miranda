# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Car:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
        
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

class Motor:
    def __init__(self, nome):
        self.nome = nome

carro1 = Car('pajero')
carro2 = Car('new fiesta')
carro3 = Car('fit')
fabricante1 = Fabricante('honda')
fabricante2 = Fabricante('ford')
motor1 = Motor(1.6)
motor2 = Motor(3.0)
carro1.motor = motor2
carro1.fabricante = fabricante1
carro2.motor = motor1
carro2.fabricante = fabricante2
carro3.motor = motor1
carro3.fabricante = fabricante1
print(carro1.nome, carro1.motor.nome, carro1.fabricante.nome)
