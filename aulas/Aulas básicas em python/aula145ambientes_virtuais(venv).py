# Ambientes virtuais em Python (venv)
# Um ambiente virtual carrega toda a sua instalação
# do Python para uma pasta no caminho escolhido.
# Ao ativar um ambiente virtual, a instalação do
# ambiente virtual será usada.
# venv é o módulo que vamos usar para
# criar ambientes virtuais.
# Você pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv env .venv .env

# projeto1

# criando ambiente virtual com venv
# Abra a pasta do seu projeto no terminal,
# digite "python -V" para saber a versão do python
# digite "python -m venv [nome do ambiente]" para criar um ambiente virtual em seu projeto
# digite "gcm python" para saber informações do programa python
# digite "-Syntax" para aparecer o local detalhado do local de armazenamento do python
# digite "which python" para saber onde o python está localizado

# Para ativar seu ambiente virtual, abra o terminal do diretório do seu projeto e
# digite"venv\Scripts\activate"
# comando "pip" mostra os subcomandos
# comando "pip --version" mostra a versão do pip
# comando "python.exe -m pip install --upgrade pip" atualiza o pip
# comando "python -m pip install pymysql" instala o pymysql !CUIDADO! CERTIFIQUE
# QUE ESTEJA INSTALANDO NO AMBIENTE VIRTUAL E NÃO GLOBAL
# comando "pip uninstall pymysql" desinstala o pymysql
# comando "pip freeze" mostra todos os packages instalados
# comando "pip index versions pymysql" mostra todas as versões do package pymysql
# comando "pip install pymysql==1.01" instala a versão digitada

# requirements.txt
# pip freeze > requirements.txt -> (criando) O arquivo requirements.txt é uma convenção
# comum no ecossistema Python. Ele serve para listar todas as dependências do seu
# projeto Python, permitindo a fácil instalação
# dessas dependências em qualquer ambiente, especialmente em ambientes virtuais.
# pip install -r .\requirements.txt -> instala todos os pacotes para seu ambiente
# pip freeze -> requiremnets.txt -> após instalar um pacote novo, precisa atualizar
# o requirements.txt com esse comando
