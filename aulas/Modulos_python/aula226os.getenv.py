# Variáveis de ambiente com Python
# Para variáveis de ambiente
# Windows PS: $env:VARIAVEL="VALOR"  #Cria a variável de ambiente
            # dir env: #lista as variáveis criadas
# Linux e Mac(terminal): export VARIAVEL="VALOR"  #Cria a variável temporariamente
             # echo $VARIAVEL #imprime
# Para obter o valor das variáveis de ambiente
# os.getenv ou os.environ['VARIAVEL']
# Para configurar variáveis de ambiente
# os.environ['VARIAVEL'] = 'valor'
# Ou usando python-dotenv e o arquivo .env
# pip install python-dotenv
# from dotenv import load_dotenv
# load_dotenv()
# https://pypi.org/project/python-dotenv/
# OBS.: sempre lembre-se de criar um .env-example CASO QUEIRA ENVIAR PARA O REPOSITÓRIO
# NUNCA ENVIE SEU ".env" para o seu repositório

import os
from dotenv import load_dotenv

# #depois de criar a variável "SENHA" 
# senha = os.getenv('SENHA') 
# print(senha)

load_dotenv() #apenas se o ".env" estiver criado para executar
print(os.environ) #lista as variáveis de ambiente
print(os.getenv('BD_USER')) #imprime o valor da variável
os.environ['BD_USER'] = 'MILENA' #ALTERANDO O VALOR
print(os.environ['BD_USER']) #imprime o valor da variável


