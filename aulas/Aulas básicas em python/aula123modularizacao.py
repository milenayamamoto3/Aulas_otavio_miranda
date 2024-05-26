# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

try:   #usa o "try" para executar primeiro o import sys
    import sys
    sys.path.append('/Users/acerc/OneDrive/Área de Trabalho') #adiciona local

except ModuleNotFoundError:
    ...

import aula123exemplo  #módulo em desktop sendo executado, pois seu local foi adc
import aula123modularizacao_m #módulo onde seu local por padrão já está adc

print('Este módulo se chama', __name__) #executado primeiro, módulo main
print(*sys.path, sep='\n') #exibe os locais onde os módulos podem ser importados
                            #o asterisco desempacota a lista, pois o path é LISTA

print(aula123modularizacao_m.variavel_1)  #dessa maneira, chamamos a variável
from aula123modularizacao_m import variavel_1  #importando a variável
print(variavel_1)  #printando a variável que já está importada

import importlib 
for i in range(10):
    importlib.reload(aula123modularizacao_m) #recarregar o módulo
    print(i)

from aula123modularizacao_m import *
print(variavel) #consegue puxar
# print(variavel_2) -> não consegue puxar, pois não está no __all__



