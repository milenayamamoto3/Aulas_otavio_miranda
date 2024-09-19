# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# Levantando e tratando suas Exceptions (Exceções)
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)
class MyError(Exception):
    ...

class OtherError(Exception):
    ...

def levantar():
    exception_ = MyError('a', 'b', 'c')
    exception_.add_note('Look at note 1')
    exception_.add_note('You wrong that')
    raise exception_

try:
    # 1/0
    levantar()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args) #args = argumneta em tupla
    print()
    #relançando outra exceção
    exception_ = OtherError('Vou lançar de nv') 
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('One more note')
    raise exception_ from error 