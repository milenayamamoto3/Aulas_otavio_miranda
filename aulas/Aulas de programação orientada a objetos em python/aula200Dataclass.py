# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, astuple, asdict, field, fields
#astuple = função "como tupla" 
#asdict =  função "como dict"
#field = função que configura os campos da dataclass
#fields = função que retorna as configurações dos campos

@dataclass
#init=False # retirando o init do @dataclass
#frozen=True #congelando os attrs
#order=True #pode-se usar "sorted()" para ordenar uma lista de classes 
class Pessoa:
    nome: str = field(default="Missing", repr=False) #padronizando valor e tirando
    #do repr
    sobrenome: str = "not sent" #valor padrão (apenas com valores imutáveis)
    idade: int = 0 #valor padrão (apenas com valores imutáveis)
    # enderecos: list[str] #não se pode colocar argumento sem valor padrão após os que tem,
    # enderecos: list[str] = [] e mesmo que colocasse, lista é mutável
    enderecos: list[str] = field(default_factory=list) #aqui resolve o problem

    # def __init__(self, nome, sobrenome) -> None: #criando meu próprio init
    #     self.nome = nome
    #     self.sobrenome = sobrenome
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'

    # def __pos__init__(self): # pos init não vai ser chamado, pois init=False
    #     print('POS INIT')
        

    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'

    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split() #é um method que divide uma str em list
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome) #é um method que concatena duas ou mais str

if __name__ == '__main__':
    # p1 = Pessoa('Luiz', 30)
    # p2 = Pessoa('Luiz', 30)
    # print(p1 == p2)

    # p1 = Pessoa('Luiz', 'Otávio')
    # p1.nome_completo = 'Maria Helena Figueredo'
    # p1.nome = 'Maria' # com o frozen=True, dará erro, pois 'nome' não pode ser alterado
    # print(p1) #caso o repr=False, retorna o local do objct
    # print(p1.nome_completo)

    # print(asdict(p1).keys()) #mostra as chaves do dict Pessoa class
    # print(asdict(p1).values()) #mostra os valores do dict Pessoa class
    # print(asdict(p1).items()) #mostra os itens contidos no dict Pessoa class
    # print(astuple(p1)[0]) #mostra o índice "0" da tupla Pessoa class

    p1 = Pessoa()
    # print(fields(p1))
    print(p1)

    #Para order=True funcionar:
    # lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    # ordenadas = sorted(lista, reverse=True) #reverse=True ativa o inverso apenas
    # print(ordenadas)

    #Quando order-False, criando minha própria ordem (MELHOR OPÇÃO):
    # lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    # ordenadas = sorted(lista, reverse=True, key=lambda p: p.nome) #ou "p.sobrenome"
    # print(ordenadas)                       #para mudar o atributo para ordenar