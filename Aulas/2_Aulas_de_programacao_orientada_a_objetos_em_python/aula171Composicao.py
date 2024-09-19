# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
    
    def inserir_enderecos(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero)) #criando a instância ENDEREÇO
      #dentro da classe CLIENTE

    def inserir_enderecos_externo(self, endereco): #adicionando end de fora 
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        #print(*self.enderecos, sep='\n') #asterisco para desempacotar e sep para 
              #quebrar a linha
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):#garbage collection = é a exclusão de objects que não tem mais uso
        print('apagando', self.nome)

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):#se o nome for apagado, seus end são apagados tb
        print('apagando', self.rua, self.numero)

cliente1 = Cliente('Maria')
cliente1.inserir_enderecos('Rua Rosa', 54)
cliente1.inserir_enderecos('Rua Sol', 100)
print(cliente1.enderecos) #aqui mostra apenas os locais dos endereços armazenados
print(cliente1.enderecos[0].rua) #pega o nome da rua pelo índice na lista
print(cliente1.enderecos[1].rua)
#cliente1.listar_enderecos() #aqui mostra apenas os locais dos endereços armazenados

endereco_externo = Endereco('Av Saudade', 12)
cliente1.inserir_enderecos_externo(endereco_externo)
cliente1.listar_enderecos()

del cliente1  #apagando o objeto antes do programa terminar

print(endereco_externo.rua, endereco_externo.numero) #antes do programa terminar, 
#ainda da pra pegar os valores do objct de fora

print('Aqui termina o código')
#quando o programa termina, o resto dos objt são deletados



