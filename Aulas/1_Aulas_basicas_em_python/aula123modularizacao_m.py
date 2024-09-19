print('Este módulo se chama', __name__)
variavel_1 = 'Milena'

__all__ = [
   'variavel',
] #nesta lista, pega apenas o que está dentro quando em outro módulo puxar tudo com 
#asterisco, só vai conseguir puxar o que está aqui dentro

variavel = 'Alguma coisa'
variavel_2 = 2