# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves (variáveis)
# safe_substitute: não gera erro, mas tb não substitui
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.

# import json
import locale
import string
from datetime import datetime
from pathlib import Path


CAMINHO_ARQUIVO = Path(__file__).parent / 'aula225.txt'

locale.setlocale(locale.LC_ALL, '')


def converte_para_brl(numero: float) -> str:
    brl = 'R$ ' + locale.currency(numero, symbol=False, grouping=True)
    return brl


data = datetime(2022, 12, 28)
dados = dict(
    nome='João',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone='+55 (11) 7890-5432'
)

# print(json.dumps(dados, indent=2, ensure_ascii=False))

text = '''
Prezado(a) ${nome},

Informamos que sua mensalidade será cobrada no valor de ${valor} no dia ${data}. 
Caso deseje cancelar o serviço, entre em contato com a ${empresa} pelo telefone ${telefone}.

Atenciosamente,

${empresa}, 
Abraços

'''
class MyTemplate(string.Template):
    delimiter = '$' # se o texto tiver outro delimiter, não substituirá

with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    text = arquivo.read()
    template = MyTemplate(text)
    print(template.substitute(dados))
   # print(template.safe_substitute(dados))




