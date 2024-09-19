def meu_repr(self):
    return f'{type(self).__name__}({self.__dict__})'


class Meta(type):
    #New cria e retorna a classe
    def __new__(mcs, name, bases, dct): #esse new pode executar tarefas antes de criar a cls
        print('METACLASS NEW')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 1234 #atributo
        cls.__repr__ = meu_repr

        if 'falar' not in cls.__dict__ or \
            not callable(cls.__dict__['falar']):
            raise NotImplementedError('Implemente falar')

        return cls

    #Call cria e retorna a instância
    def __call__(cls, *args, **kwargs):
        instancia = super().__call__(*args, **kwargs)

        if 'nome' not in instancia.__dict__:
            raise NotImplementedError('Crie o attr nome')
        
        # print(instancia.__dict__)

        return instancia


class Pessoa(metaclass=Meta):
    # falar = 123 #is not callable

    def __new__(cls, *args, **kwargs):
        print('MEU NEW')
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, nome):
        print('MEU INIT')
        self.nome = nome

    def falar(self): #is callable , essa função retorna None (sem valor)
        print('FALANDO...')
    


p1 = Pessoa('Luiz')
# print(p1.attr)
# print(Pessoa.attr)
# print(p1) #Quando print(p1) é chamado, tenta imprimir a representação da instância
# print(p1.falar()) #busca o valor do método
# p1.falar() #não busca o valor do método

 