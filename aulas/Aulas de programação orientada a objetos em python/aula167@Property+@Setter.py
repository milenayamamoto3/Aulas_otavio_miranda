# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯
class Caneta:
    def __init__(self, cor):
        # private protected
        self.cor = cor #sem underline, está chamado o setter
        self._cor_tampa = None 

    @property #chama valor do atributo em __init__
    def cor(self):
        print('ESTOU NO GETTER')
        return self._cor

    @cor.setter #configura atributo em método
    def cor(self, valor):
        #if not isinstance(valor, str):
        #    raise TypeError("O nome deve ser uma string")
        print('ESTOU NO SETTER')
        self._cor = valor

    @property
    def cor_tampa(self):
        print('getter da cor da tampa')
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        print('setter da cor da tampa')
        self._cor_tampa = valor


caneta = Caneta('Azul')
caneta.cor = 'Rosa'
caneta.cor_tampa = 'Azul'
print(caneta.cor)
print(caneta.cor_tampa)