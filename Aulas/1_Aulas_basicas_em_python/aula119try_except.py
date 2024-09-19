# try e except para tratar exceções
# Vários tipos de Exceptions no link abaixo:
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions 

try:
    a = 18
    b = 0
    c = a / b
    print(b[0])
    print('Linha 1'[1000])
    print('Linha 2')
except ZeroDivisionError:
    print('Dividiu por zero.') #quando 'b' = 0
except NameError:
    print('Nome b não está definido') #quando comenta o 'b'
except (TypeError, IndexError) as error: #cria uma variável para a INSTANCE do erro
    print('TypeError + IndexError') #quando tenta pegar o índice de 'b'
                                    #quando tenta pegar um índice que n existe
    print('MSG:', error) # imprime a instance do erro        
    print('Nome da classe de erro:', error.__class__.__name__) # imprime o nome do erro  
except Exception:                   
    print('ERRO DESCONHECIDO.')     #pega todos os outros erros

print('CONTINUAR')