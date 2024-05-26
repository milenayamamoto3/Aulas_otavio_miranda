
class Somar:
    def __init__(self, func):
        self.func = func #objeto é a função

    def __call__(self, *args, **kwargs):
        print(args, kwargs)
        return self.func(*args, **kwargs)

@Somar #decorator inicia com letra maiúscula quer dizer que é de decorator class
def soma(x, y):
    return x + y

soma_x_y = soma(2, 4)
print(soma_x_y)

##########################

class Somar2:
    def __init__(self, func): 
        self.func = func
        self._multiplicador = 10

    def __call__(self, *args, **kwargs):
        resultado = self.func(*args, **kwargs)
        return resultado * self._multiplicador

@Somar2 
def somar(x, y):
    return x + y

soma_x_y_2 = somar(2, 4)
print(soma_x_y_2)

##########################

class Somar3:
    def __init__(self, multiplicador): #objeto é o do decorator
        self._multiplicador = multiplicador

    def __call__(self, func):
        def interno(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return interno

@Somar3(10) 
def somarr(x, y):
    return x + y

soma_x_y_3 = somarr(2, 4)
print(soma_x_y_3)