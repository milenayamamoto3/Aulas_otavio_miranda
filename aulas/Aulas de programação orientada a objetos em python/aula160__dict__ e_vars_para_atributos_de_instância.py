# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


dados = {'nome': 'João', 'idade': 35}
p1 = Pessoa(**dados)

# p1.nome = 'EITA' # mudar de nome
# p1.__dict__['outra'] = 'coisa' #  __dict__ é editável, não é só leitura  
# p1.__dict__['nome'] = 'EITA'
# del p1.__dict__['nome']
# print(p1.__dict__)

print(vars(p1)) # vars mostra a variável em dicionário
print(p1.nome)