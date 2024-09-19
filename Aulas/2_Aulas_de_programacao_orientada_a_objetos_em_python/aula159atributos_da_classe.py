# Atributos de classe
class Pessoa:
    ano_atual = 2022 #atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 100 #atributo da instância

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)

print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1 ->fora do escopo da pra alterar o atributo da classe

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())