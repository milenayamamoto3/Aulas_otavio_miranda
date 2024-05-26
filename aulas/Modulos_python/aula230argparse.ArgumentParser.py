# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-b', '--basic',
    help='Mostra "Olá mundo" na tela',
    # type=str, # Tipo do argumento
    metavar='STRING',
    # default='Olá mundo', # Valor padrão   
    required=False, # argumentos "-b/--basic" são requeridos 
    # nargs='+', # pode-se ter mais args (lista)
    action='append')  # Recebe o argumento mais de uma vez 
# o segundo argumento elimina o primeiro

parser.add_argument(
    '-v', '--verbose',
    help='Mostra logs',
    action='store_true' # True caso tenha o "-v" no terminal e False quando sem
)

args = parser.parse_args()

# print(args.b)
# terminal, 
# -b 123 -> "123"
# -b -> "usage: aula230argparse.ArgumentParser.py [-h] [-b B]
       # aula230argparse.ArgumentParser.py: error: argument -b: expected one argument"
# None -> None

if args.basic is None:
    print('Você não passou o valor de basic.')
    print(args.basic) 
else:
    print('O valor de basic:', args.basic)
# terminal,
# -b 123 -> "O valor de basic: 123"

print(args.verbose) 

#(myvenv) PS C:\Users\acerc\OneDrive\Área de Trabalho\Aulas_python\Aulas_otavio_miranda\aulas\Modulos_python> 
#python aula230argparse.ArgumentParser.py -b 123 -b "A" -b "b" -v
# terminal : O valor de basic: ['123', 'A', 'b']
           # False