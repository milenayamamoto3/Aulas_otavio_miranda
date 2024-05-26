# raise - lançando exceções (erros)
# Abaixo no link, os tipos de erros Exceptions:
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

# raise ZeroDivisionError('Não pode dividir por zero') #nomeia a INSTANCE do erro e 
# #ao lançá-lo, o resto abaixo não executará, pois você lançou um erro

# def funcao(n, m):
#     try:
#         return n / m
#     except ZeroDivisionError:
#         print('_____')
#         raise #lança o erro
# print(funcao(8, 0))

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    return True

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)): # if not TRUE
        raise TypeError(
            f'"{n}" deve ser int ou float.'
            f'"{tipo_n.__name__}" enviado.' # a função "name" retorna apenas o nome da classe
        )
    return True

def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n / d

print(divide(8, '0'))