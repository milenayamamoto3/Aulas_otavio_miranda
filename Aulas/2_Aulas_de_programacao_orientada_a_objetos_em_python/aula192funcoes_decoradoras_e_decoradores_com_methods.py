def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

        if 'Terra' in resultado:
            return 'Você está em casa'
        
        return resultado
    return interno

class Planeta:
    def __init__(self, nome):
        self.nome = nome
    
    @meu_planeta
    def falar_nome(self):
        return f'O planeta é {self.nome}'
    
terra = Planeta('Terra')
print(terra.falar_nome())
marte = Planeta('Marte')
print(marte.falar_nome())