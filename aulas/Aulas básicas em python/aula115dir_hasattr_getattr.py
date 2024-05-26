# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'upper'

print(dir(string)) # função que mostra todos os nomes definidos em str

if hasattr(string, metodo): # confere se existe o método para este objeto
    print(f'Existe {metodo}')
    print(getattr(string, metodo)()) # executa o método desse objeto
else:
    print('Não existe o método', metodo)