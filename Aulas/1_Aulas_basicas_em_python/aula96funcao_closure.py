"""
Closure e funções que retornam outras funções
"""
def funcao(nome, texto):
    def saudar():
        return f'{nome}, {texto}'
    return saudar #com parênteses - executa a função saudar(), sem - retorna código da memória

s1 = funcao('Bom dia', 'Milena')
s2 = funcao('Bom dia', 'Manami')
print(s1()) #parênteses internos são chamados de "closure", eles fazem a execução da função interna
print(s2()) #mas para isso, o "return saudar", precisa está sem os parênteses


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))