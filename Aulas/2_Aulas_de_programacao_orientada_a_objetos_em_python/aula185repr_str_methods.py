
class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self): 
        return f'({self.x}, {self.y})'

    def __repr__(self): #para dev
        # class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'
#colocamos a "!r" tb nos parâmetros para especificar no caso d str 'String' ser uma str

p1 = Ponto(1, 2)
p2 = Ponto(978, 876)
print(p1) #automaticamente chamando a str method
print(repr(p2)) #chamando repr method
print(f'{p2}') #claramente chamando a str method
print(f'{p2!r}') #chamando o repr dentro da fstr