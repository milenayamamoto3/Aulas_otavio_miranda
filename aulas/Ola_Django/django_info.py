# criando um projeto :
# 1 - dir com o "manage.py" inside
# django-admin startproject nomedoProjeto
# * manage.py tem a mesma função de django-admin
# 2 - dir com o "manage.py" out
# django-admin startproject nomedoProjeto .

# "rodando"
# python manage.py runserver

# coletar arquivos estáticos para static_files
# python manage.py collectstatic

# quando o debug é false e tem hosts permitidos usa-se apenas o static_files
# pois não está mais em construção (está pronto)
"""
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]
"""

# Quando debug é true(em construção),
# você pode usar normal os arquivos státicos do apps
"""
DEBUG = True

"""

# deletando um projeto:
# rmdir NomeDoProjeto

# sair (no terminal):
# crtl + c

# atualizando o gitignore:
# git rm -r --cached .
# git add . -> git commit -m "." -> git push origin main

# python manage.py --hep -> mostra os comandos
# python manage.py startapp home -> cria um app chamado "home"
# python manage.py startapp blog -> cria um app chamado "blog"

# ctrl+p -> procura na barra o arquivo pelo nome
