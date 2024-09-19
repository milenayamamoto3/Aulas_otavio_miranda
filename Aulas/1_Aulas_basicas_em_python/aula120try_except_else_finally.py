# try, except, else e finally

try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU ZERO')
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):
    print('NameError, ImportError')
else: #se não der erro, else executará
    print('Não deu erro')
finally: #sempre executará tendo erro ou n
    print('FECHAR ARQUIVO')
    # não existe try e else apenas e nem cada um deles sozinho 