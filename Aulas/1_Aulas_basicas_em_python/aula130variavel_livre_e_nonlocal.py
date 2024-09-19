# Variáveis livres + nonlocal (locals, globals)
# print(globals()) -> função global sem argumento, retorna todos os símbolos globais deste módulo por dict
def fora(x):
    a = x

    def dentro():
        print(locals()) #função local sem argumento dentro da função"dentro" retorna variáveis locais por dict
        
        return a
    return dentro

dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print(dentro2())

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final # nonlocal consegue alterar a variável da funçaõ externa
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)